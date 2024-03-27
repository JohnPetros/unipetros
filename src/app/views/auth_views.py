from flask import Blueprint, request, render_template, flash, redirect, url_for

from forms.login_form import LoginForm

from use_cases.auth import login_use_case

from auth import AuthUser, logout as logout_user, login_checker

auth_views = Blueprint("auth_views", __name__)


@auth_views.route("/login", methods=["GET", "POST"])
def login() -> str:
    login_form = LoginForm()

    if request.method == "GET":
        return render_template("pages/home/login/index.html", login_form=login_form)

    if request.method == "POST" and login_form.validate_on_submit():
        auth_user = login_use_case.execute(
            email=login_form.email.data,
            password=login_form.password.data,
            should_remember_user=login_form.remember_me.data,
            role="admin",
        )

        if isinstance(auth_user, AuthUser):
            next_page_param = request.args.get("next")

            if next_page_param:
                print(next_page_param)
                return redirect(next_page_param)

            flash(f"Bem-vindo, {auth_user.name} 😁", "success")
            return redirect(url_for("admin_views.get_analytics_page"))

    flash("E-mail ou senha incorretos", "error")
    return render_template("pages/home/login/index.html", login_form=login_form)


@auth_views.route("/logout")
@login_checker
def logout() -> str:
    logout_user()

    return redirect(url_for("auth_views.login"))
