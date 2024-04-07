from flask import render_template, request
from werkzeug.datastructures import ImmutableMultiDict

from core.use_cases.admin import (
    create_professor,
)

from infra.auth import login_checker, role_checker
from infra.forms.professor_form import ProfessorForm


@login_checker
@role_checker("admin")
def create_professor_view() -> str:
    form_data = request.form.to_dict()
    form_data["avatar"] = request.files["avatar"]

    professor_form = ProfessorForm(ImmutableMultiDict(form_data))

    updated_professors = []

    if professor_form.validate_on_submit():
        updated_professors = create_professor.execute(form_data)

    return render_template(
        "pages/admin/professors/table/index.html",
        professors=updated_professors,
    )
