from flask import render_template, request

from core.use_cases.admin import create_courses_by_csv

from infra.auth import login_checker, role_checker


@login_checker
@role_checker("admin")
def create_courses_by_csv_view() -> str:
    updated_courses = create_courses_by_csv.execute(request.files["csv"])

    return render_template(
        "pages/admin/courses/table/index.html", courses=updated_courses
    )
