from flask import render_template, request

from auth import get_auth_user, login_checker, role_checker

from use_cases.admin import get_professors_page_data_use_case, create_professor_use_case


@login_checker
@role_checker("admin")
def handle_professors_page_view() -> str:
    user = get_auth_user()

    professors_page_data = get_professors_page_data_use_case.execute()

    professors = professors_page_data["professors"]
    professor_form = professors_page_data["professor_form"]

    if request.method == "POST" and professor_form.validate_on_submit():
        updated_professors = create_professor_use_case.execute(professor_form.data)
        professors = updated_professors

    return render_template(
        "pages/admin/professors/index.html",
        user=user,
        professors=professors,
        professor_form=professor_form,
    )
