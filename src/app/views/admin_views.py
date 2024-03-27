from flask import Blueprint, render_template, request

from auth import get_auth_user, login_checker, role_checker

from use_cases.admin import (
    get_professors_page_data_use_case,
    get_professor_details_page_data_use_case,
    create_professor_use_case,
    create_professors_by_csv_use_case,
    get_subjects_page_data_use_case,
    create_subject_use_case,
)

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

    professors_page_data = get_professors_page_data_use_case.execute()

    professors = professors_page_data["professors"]
    professor_form = professors_page_data["professor_form"]

    if request.method == "POST" and professor_form.validate_on_submit():
        updated_professors = create_professor_use_case.execute(professor_form.data)
        professors = updated_professors

    return render_template(
        "pages/admin/professors/index.html",
        user=user,
        professors=professors,
        professor_form=professor_form,
    )


@admin_views.route("/dashboard/professors/csv", methods=["POST"])
@login_checker
@role_checker("admin")
def create_professors_by_csv() -> str:
    updated_professors = create_professors_by_csv_use_case.execute(request.files["csv"])

    return render_template(
        "pages/admin/professors/table/index.html", professors=updated_professors
    )


@admin_views.route("/dashboard/professors/<professor_id>")
@login_checker
@role_checker("admin")
def get_professor_details_page(professor_id) -> str:
    user = get_auth_user()
    get_professor_details_page_data_use_case.execute(professor_id)

    return render_template("pages/admin/professor/index.html", user=user)


@admin_views.route("/dashboard/subjects", methods=["GET", "POST"])
@login_checker
@role_checker("admin")
def get_subjects_page() -> str:
    user = get_auth_user()

    subjects_page_data = get_subjects_page_data_use_case.execute()

    subjects = subjects_page_data["subjects"]
    subject_form = subjects_page_data["subject_form"]

    if request.method == "POST" and subject_form.validate_on_submit():
        updated_subjects = create_subject_use_case.execute(subject_form.data)
        subjects = updated_subjects

    return render_template(
        "pages/admin/subjects/index.html",
        user=user,
        subjects=subjects,
        subject_form=subject_form,
    )


@admin_views.route("/dashboard/subjects", methods=["GET", "POST"])
@login_checker
@role_checker("admin")
def create_subjects_by_csv() -> str:
    user = get_auth_user()

    subjects_page_data = get_subjects_page_data_use_case.execute()

    subjects = subjects_page_data["subjects"]
    subject_form = subjects_page_data["professor_form"]

    if request.method == "POST" and subject_form.validate_on_submit():
        updated_subjects = create_subject_use_case.execute(subject_form.data)
        subjects = updated_subjects

    return render_template(
        "pages/admin/subjects/index.html",
        user=user,
        subjects=subjects,
        subject_form=subject_form,
    )
