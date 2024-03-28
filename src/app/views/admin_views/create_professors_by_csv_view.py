from flask import render_template, request

from auth import login_checker, role_checker

from use_cases.admin_use_cases import create_professors_by_csv_use_case


@login_checker
@role_checker("admin")
def create_professors_by_csv_view() -> str:
    updated_professors = create_professors_by_csv_use_case.execute(request.files["csv"])

    return render_template(
        "pages/admin/professors/table/index.html", professors=updated_professors
    )
