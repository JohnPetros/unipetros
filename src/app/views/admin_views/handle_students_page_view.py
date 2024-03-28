from flask import request, render_template

from auth import get_auth_user, login_checker, role_checker

from use_cases.admin import get_students_page_data_use_case, create_subject_use_case


@login_checker
@role_checker("admin")
def handle_students_page_view() -> str:
    user = get_auth_user()

    students_page_data = get_students_page_data_use_case.excute()

    students = students_page_data["students"]
    student_form = students_page_data["student_form"]

    if request.method == "POST" and student_form.validate_on_submit():
        updated_students = create_subject_use_case.execute(student_form.data)
        students = updated_students

    return render_template(
        "pages/admin/students/index.html",
        user=user,
        students=students,
        student_form=student_form,
    )
