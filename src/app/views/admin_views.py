from flask import Blueprint, render_template

admin_views = Blueprint("admin_views", __name__)


@admin_views.route("/analytics")
def get_analytics_page() -> str:
    return render_template("pages/admin/analytics/index.html")
