from flask import Flask, flash

from .home_views import home_views
from .auth_views import auth_views
from .admin_views import admin_views


def init_views(app: Flask) -> None:
    app.register_blueprint(auth_views)
    app.register_blueprint(home_views)
    app.register_blueprint(admin_views)

    @app.errorhandler(404)
    def handle_not_found_error(_):
        return "EITA"

    @app.errorhandler(500)
    def handle_bad_request_error(error):
        flash(error.description, "error")
        return "PROBLEMA GRAVE NO SERVIDOR"
