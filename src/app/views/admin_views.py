from flask import Blueprint, render_template, redirect, url_for, request

from auth import get_auth_user, login_checker, role_checker

from controllers.admin import (
    get_professors_page_data_controller,
    get_professor_page_data_controller,
    create_new_professor_controller,
    create_professors_by_csv_controller,
)

from forms.professor_form import ProfessorForm

admin_views = Blueprint("admin_views", __name__)


@admin_views.route("/dashboard/analytics")
@login_checker
@role_checker("admin")
def get_analytics_page() -> str:
    user = get_auth_user()
    return render_template("pages/admin/analytics/index.html", user=user)


@admin_views.route("/dashboard/professors", methods=["GET", "POST"])
@login_checker
@role_checker("admin")
def get_professors_page() -> str:
    user = get_auth_user()

    professors_page_data = get_professors_page_data_controller.execute()

    professors = professors_page_data["professors"]
    professor_form = professors_page_data["professor_form"]

    if request.method == "POST" and professor_form.validate_on_submit():
        updated_professors = create_new_professor_controller.execute(
            professor_form.data
        )
        professors = updated_professors

    return render_template(
        "pages/admin/professors/index.html",
        user=user,
        professors=professors,
        professor_form=professor_form,
    )


@admin_views.route("/dashboard/professor", methods=["POST"])
@login_checker
@role_checker("admin")
def create_professor() -> str:
    professor_form = ProfessorForm()

    professor_form.validate()

    return redirect(url_for("admin_views.get_professors_page"))


@admin_views.route("/dashboard/professors/csv", methods=["POST"])
@login_checker
@role_checker("admin")
def create_professors_by_csv() -> str:
    create_professors_by_csv_controller.execute(request.files["csv"])
    return "EITA"


@admin_views.route("/dashboard/professors/<professor_id>")
@login_checker
@role_checker("admin")
def get_professor_page(professor_id) -> str:
    user = get_auth_user()
    get_professor_page_data_controller.execute(professor_id)

    return render_template("pages/admin/professor/index.html", user=user)
