from flask import Blueprint

from .get_landing_page_view import get_landing_page_view
from .get_about_page_view import get_about_page_view
from .get_contact_page_view import get_contact_page_view

home_views = Blueprint("home_views", __name__)

route = home_views.add_url_rule

route(rule="/", view_func=get_landing_page_view)

route(rule="/about", view_func=get_about_page_view)

route(rule="/contact", view_func=get_contact_page_view)
