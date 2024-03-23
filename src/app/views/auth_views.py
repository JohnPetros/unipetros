from flask import Blueprint, request, render_template, flash, redirect, url_for

from forms.login_form import LoginForm
from controllers.users_controller import UsersController
from models.user_model import UserModel
from auth import AuthUser, login as login_user, logout as logout_user

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
            is_login_success = login_user(
                auth_user, should_remember_user=login_form.remember_me.data
            )

            if is_login_success:
                next_page_param = request.args.get("next")

                if next_page_param:
                    print(next_page_param)
                    return redirect(next_page_param)

                flash(f"Bem-vindo, {user.name} 😁", "success")
                return redirect(url_for("admin_views.get_analytics_page"))

    flash("E-mail ou senha incorretos", "error")
    return render_template("pages/home/login/index.html", login_form=login_form)


@auth_views.route("/logout", methods=["GET", "POST"])
def logout() -> str:
    logout_user()

    return redirect(url_for("auth_views.login"))
