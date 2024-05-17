from flask import render_template, request
from werkzeug.datastructures import ImmutableMultiDict


from core.use_cases.admin import get_filtered_professors, create_professor
from infra.utils.error import Error

from infra.auth import login_checker, role_checker
from infra.forms.professor_form import ProfessorForm


@login_checker
@role_checker("admin")
def create_professor_by_form_view() -> str:
    search = request.args.get("search")
    gender = request.args.get("gender", "all")
    subjects_ids = request.args.getlist("subjects_ids[]")
    page = request.args.get("page", 1)

    form_data = request.form.to_dict()

    if "avatar" in request.files:
        form_data["avatar"] = request.files["avatar"]

    try:
        professor_form = ProfessorForm(ImmutableMultiDict(form_data))

        if not professor_form.validate_on_submit():
            raise Error("Formulário inválido", status_code=400)

        create_professor.execute(
            {
                "email": professor_form.email.data,
                "name": professor_form.name.data,
                "avatar": professor_form.avatar.data,
                "password": professor_form.password.data,
                "phone": professor_form.phone.data,
                "gender": professor_form.gender.data,
                "birthdate": professor_form.birthdate.data,
                "subjects": request.form.getlist("subjects[]"),
            }
        )

        professors, pages_count = get_filtered_professors.excute(
            gender=gender,
            name_or_email=search,
            page_number=page,
            subjects_ids=subjects_ids,
        )

        return render_template(
            "pages/admin/professors/table/index.html",
            professors=professors,
            pages_count=pages_count,
            success_message="Professor criado com sucesso",
        )
    except Error as error:
        print(professor_form.errors, flush=True)
        return (
            render_template(
                "pages/admin/professors/create_professor_form/fields.html",
                professor_form=professor_form,
                error_message=error.ui_message,
            ),
            error.status_code,
        )
