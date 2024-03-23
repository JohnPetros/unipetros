from flask import Blueprint, request, render_template, flash, redirect, url_for

from forms.login_form import LoginForm
from controllers.users_controller import UsersController
from models.user_model import UserModel
from auth import AuthUser, login as login_user

auth_views = Blueprint("auth_views", __name__)

users_controller = UsersController()


@auth_views.route("/login", methods=["GET", "POST"])
def login() -> str:
    login_form = LoginForm()

    if request.method == "GET":
        return render_template("pages/home/login/index.html", login_form=login_form)

    if request.method == "POST" and login_form.validate_on_submit():
        user = users_controller.handle_login(
            email=login_form.email.data, password=login_form.password.data
        )

        if isinstance(user, UserModel):
            auth_user = AuthUser(user)
            is_login_success = login_user(auth_user)
            if is_login_success:
                return redirect(url_for("admin_views.get_analytics_page"))

    flash("E-mail ou senha incorretos", "error")
    return render_template("pages/home/login/index.html", login_form=login_form)


@auth_views.route("/logout", methods=["GET", "POST"])
def logout() -> str:
    login_form = LoginForm()

    flash("E-mail ou senha incorretos", "error")

    if request.method == "GET":
        return render_template("pages/home/login/index.html", login_form=login_form)

    return render_template("pages/home/login/index.html", login_form=login_form)
