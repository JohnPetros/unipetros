from flask import Blueprint, render_template
from auth import get_auth_user, login_checker, role_checker
from controllers.admin_controller import AdminController

admin_views = Blueprint("admin_views", __name__)

admin_controller = AdminController()


@admin_views.route("/dashboard/analytics")
@login_checker
@role_checker("admin")
def get_analytics_page() -> str:
    user = get_auth_user()
    return render_template("pages/admin/analytics/index.html", user=user)


@admin_views.route("/dashboard/professors")
@login_checker
@role_checker("admin")
def get_professors_page() -> str:
    user = get_auth_user()

    professors = admin_controller.get_professors()

    return render_template(
        "pages/admin/professors/index.html", user=user, professors=professors
    )
