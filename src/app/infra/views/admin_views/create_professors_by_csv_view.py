from math import ceil

from flask import render_template, request

from core.use_cases.admin import create_professors_by_csv, get_filtered_professors
from core.constants.pagination_limit import PAGINATION_LIMIT

from infra.auth import login_checker, role_checker


@login_checker
@role_checker("admin")
def create_professors_by_csv_view() -> str:
    search = request.args.get("search")
    subjects_ids = request.args.getlist("subjects_ids[]")
    gender = request.args.get("gender", "all")
    page = request.args.get("page", 1)

    csv = request.files["csv"]
    create_professors_by_csv.execute(csv)

    professors = get_filtered_professors.excute(
        name_or_email=search, subjects_ids=subjects_ids, page_number=page, gender=gender
    )[0]

    return render_template(
        "pages/admin/professors/table/index.html",
        professors=professors,
        pages_count=ceil(len(professors) / PAGINATION_LIMIT),
        success_message="Professores criados com sucesso",
    )
