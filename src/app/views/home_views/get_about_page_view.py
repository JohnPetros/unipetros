from flask import render_template


def get_about_page_view() -> str:
    return render_template("pages/home/about/index.html")
