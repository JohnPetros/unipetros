from flask import render_template, request

from core.use_cases.admin import create_students_by_csv

from infra.auth import login_checker, role_checker


@login_checker
@role_checker("admin")
def create_students_by_csv_view() -> str:
    updated_students = create_students_by_csv.execute(request.files["csv"])

    return render_template(
        "pages/admin/students/table/index.html", students=updated_students
    )
