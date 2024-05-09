from flask import redirect, url_for

from infra.auth import logout as logout_user, login_checker


@login_checker
def logout_view() -> str:
    logout_user()

    return redirect(url_for("auth_views.login_view"))
