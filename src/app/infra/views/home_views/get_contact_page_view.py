from flask import render_template


def get_contact_page_view() -> str:
    return render_template("pages/home/contact/index.html")
