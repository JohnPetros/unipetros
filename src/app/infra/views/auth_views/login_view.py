from flask import request, render_template, flash, redirect, url_for

from core.use_cases.auth import login_user

from infra.forms.login_form import LoginForm
from infra.auth import AuthUser


def login_view() -> str:
    login_form = LoginForm()

    if request.method == "GET":
        return render_template("pages/home/login/index.html", login_form=login_form)

    if request.method == "POST" and login_form.validate_on_submit():
        auth_user = login_user.execute(
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
            return redirect(url_for("admin_views.get_analytics_page_view"))

    flash("E-mail ou senha incorretos", "error")
    return render_template("pages/home/login/index.html", login_form=login_form)
