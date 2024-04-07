from flask import render_template

from infra.auth import get_auth_user, login_checker, role_checker

from core.use_cases.admin import get_professor_details_page_data


@login_checker
@role_checker("admin")
def get_professor_details_page_view(professor_id) -> str:
    user = get_auth_user()
    get_professor_details_page_data.execute(professor_id)

    return render_template("pages/admin/professor/index.html", user=user)
