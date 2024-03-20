from flask import Blueprint, render_template


home_views = Blueprint("home_views", __name__)


@home_views.route("/")
def get_home_index_page() -> str:
    return render_template("/pages/home/index.html")
