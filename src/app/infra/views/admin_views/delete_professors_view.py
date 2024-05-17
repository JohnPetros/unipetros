from math import ceil

from flask import render_template, request


from core.use_cases.admin import delete_professors, get_filtered_professors

from infra.auth import login_checker, role_checker
from infra.utils.error import Error


@login_checker
@role_checker("admin")
def delete_professors_view() -> str:
    professors_ids = request.form.getlist("professors_ids[]")

    search = request.args.get("search")
    subjects_ids = request.args.getlist("subjects_ids[]")
    page = request.args.get("page", 1)

    try:
        delete_professors.execute(professors_ids)
        professors, pages_count = get_filtered_professors.excute(
            name_or_email=search, subjects_ids=subjects_ids, page_number=page
        )
    except Error as error:
        return (
            render_template(
                "components/toast_message.html",
                message=error.ui_message,
                category="error",
            ),
            error.status_code,
        )

    return render_template(
        "pages/admin/professors/table/index.html",
        professors=professors,
        pages_count=pages_count,
        success_message="Professor(s) deletado(s) com sucesso",
    )
