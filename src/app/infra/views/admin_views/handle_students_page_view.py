from flask import request, render_template

from core.use_cases.admin import (
    get_students_page_data,
    create_student,
)

from infra.auth import get_auth_user, login_checker, role_checker


@login_checker
@role_checker("admin")
def handle_students_page_view() -> str:
    user = get_auth_user()

    students_page_data = get_students_page_data.excute()

    students = students_page_data["students"]
    student_form = students_page_data["student_form"]

    if request.method == "POST" and student_form.validate_on_submit():
        updated_students = create_student.execute(student_form.data)
        students = updated_students

    return render_template(
        "pages/admin/students/index.html",
        user=user,
        students=students,
        student_form=student_form,
    )
