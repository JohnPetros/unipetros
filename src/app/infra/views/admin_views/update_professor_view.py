from flask import request, render_template
from werkzeug.datastructures import ImmutableMultiDict

from core.use_cases.admin import update_professor

from infra.forms.professor_form import ProfessorForm
from infra.repositories import professors_repository
from infra.utils.error import Error


def update_professor_view(id: str):
    form_data = request.form.to_dict()

    if "avatar" in request.files:
        form_data["avatar"] = request.files["avatar"]

    try:
        professor_form = ProfessorForm(ImmutableMultiDict(form_data))

        if not professor_form.validate_on_submit():
            raise Error("Formulário inválido", status_code=400)

        result = update_professor.execute(
            {
                "id": id,
                "name": professor_form.name.data,
                "email": professor_form.email.data,
                "avatar": professor_form.avatar.data,
                "phone": professor_form.phone.data,
                "gender": professor_form.gender.data,
                "birthdate": professor_form.birthdate.data,
                "password": professor_form.password.data,
                "subjects_ids": request.form.getlist("subjects[]"),
            }
        )

        updated_professor = result["updated_professor"]
        related_professors = result["related_professors"]

        return render_template(
            "pages/admin/professor_details/professor.html",
            professor=updated_professor,
            related_professors=related_professors,
            message="Professor adicionado com sucesso",
        )
    except Error as error:
        if professor_form.avatar.data is None:
            professor = professors_repository.get_professor_by_id(id)
            professor_form.avatar.data = professor.avatar

        return (
            render_template(
                "pages/admin/professor_details/update_professor_form/fields.html",
                professor_form=professor_form,
                error_message=error.ui_message,
            ),
            error.status_code,
        )
