from flask import Flask
from .home_views import home_views


def init_views(app: Flask) -> None:
    app.register_blueprint(home_views)
