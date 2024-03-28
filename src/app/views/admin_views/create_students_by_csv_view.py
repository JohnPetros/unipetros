from flask import render_template, request

from auth import login_checker, role_checker

from use_cases.admin_use_cases import create_students_by_csv_use_case


@login_checker
@role_checker("admin")
def create_students_by_csv_view() -> str:
    updated_students = create_students_by_csv_use_case.execute(request.files["csv"])

    return render_template(
        "pages/admin/students/table/index.html", students=updated_students
    )
