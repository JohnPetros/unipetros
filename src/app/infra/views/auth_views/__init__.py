from flask import Blueprint

from .login_view import login_view
from .logout_view import logout_view

auth_views = Blueprint("auth_views", __name__)

route = auth_views.add_url_rule

route(rule="/login", view_func=login_view, methods=["GET", "POST"])

route(rule="/logout", view_func=logout_view)
