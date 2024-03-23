from flask import Blueprint, render_template
from auth import get_auth_user

admin_views = Blueprint("admin_views", __name__)


@admin_views.route("/analytics")
def get_analytics_page() -> str:
    user = get_auth_user()
    return render_template("pages/admin/analytics/index.html", user=user)
