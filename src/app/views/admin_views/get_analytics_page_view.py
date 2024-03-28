from flask import render_template

from auth import get_auth_user, login_checker, role_checker


@login_checker
@role_checker("admin")
def get_analytics_page_view() -> str:
    user = get_auth_user()
    return render_template("pages/admin/analytics/index.html", user=user)
