from flask import Flask

from .home_views import home_views
from .auth_views import auth_views
from .admin_views import admin_views


def init_views(app: Flask) -> None:
    app.register_blueprint(home_views)
    app.register_blueprint(auth_views)
    app.register_blueprint(admin_views)
