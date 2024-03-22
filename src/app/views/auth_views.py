from flask import Blueprint, request, render_template, flash

from forms.login_form import LoginForm


auth_views = Blueprint("auth_views", __name__)


@auth_views.route("/login", methods=["GET", "POST"])
def login() -> str:
    login_form = LoginForm()

    flash("E-mail ou senha incorretos", "error")

    if request.method == "GET":
        return render_template("pages/home/login/index.html", login_form=login_form)

    return render_template("pages/home/login/index.html", login_form=login_form)


@auth_views.route("/logout", methods=["GET", "POST"])
def logout() -> str:
    login_form = LoginForm()

    flash("E-mail ou senha incorretos", "error")

    if request.method == "GET":
        return render_template("pages/home/login/index.html", login_form=login_form)

    return render_template("pages/home/login/index.html", login_form=login_form)
