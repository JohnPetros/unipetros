from os import getenv

from flask import Flask

from views import register_views


def create_app() -> Flask:
    app = Flask(
        __name__, template_folder="../ui/templates", static_folder="../ui/static"
    )

    app.config["SECRET_KEY"] = getenv("SECRET_KEY")

    register_views(app)

    return app
