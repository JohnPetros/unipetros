from flask import Blueprint, render_template

from constants.advantages import ADVANTAGES
from constants.posts import POSTS

home_views = Blueprint("home_views", __name__)


@home_views.route("/")
def get_landing_page() -> str:
    return render_template(
        "/pages/home/landing/index.html", advantages=ADVANTAGES, posts=POSTS
    )


@home_views.route("/about")
def get_about_page() -> str:
    return render_template(
        "/pages/home/about/index.html", advantages=ADVANTAGES, posts=POSTS
    )
