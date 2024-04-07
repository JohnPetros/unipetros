from flask import render_template

from core.constants.advantages import ADVANTAGES
from core.constants.posts import POSTS


def get_landing_page_view() -> str:
    return render_template(
        "pages/home/landing/index.html", advantages=ADVANTAGES, posts=POSTS
    )
