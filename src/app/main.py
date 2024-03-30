from os import getenv


from views import init_views
from auth import init_auth

from flask import Flask

x = "eita ggggg"


def init_app() -> Flask:
    app = Flask(
        __name__, template_folder="../ui/templates", static_folder="../ui/static"
    )

    eitaEITA = "petros"

    app.config["SECRET_KEY"] = getenv("SECRET_KEY")

    init_views(app)
    init_auth(app)

    return app
