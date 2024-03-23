from os import getenv

from flask import Flask

from views import init_views
from auth import init_auth


def create_app() -> Flask:
    app = Flask(
        __name__, template_folder="../ui/templates", static_folder="../ui/static"
    )

    app.config["SECRET_KEY"] = getenv("SECRET_KEY")

    init_views(app)
    init_auth(app)

    return app
