from os import getenv

from flask import Flask

from infra.views import init_views
from infra.auth import init_auth


def init_app() -> Flask:
    app = Flask(
        __name__, template_folder="../ui/templates", static_folder="../ui/static"
    )

    app.config["SECRET_KEY"] = getenv("SECRET_KEY")

    init_views(app)
    init_auth(app)

    return app
