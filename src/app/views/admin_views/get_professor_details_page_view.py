from flask import render_template

from auth import get_auth_user, login_checker, role_checker

from use_cases.admin_use_cases import get_professor_details_page_data_use_case


@login_checker
@role_checker("admin")
def get_professor_details_page_view(professor_id) -> str:
    user = get_auth_user()
    get_professor_details_page_data_use_case.execute(professor_id)

    return render_template("pages/admin/professor/index.html", user=user)
