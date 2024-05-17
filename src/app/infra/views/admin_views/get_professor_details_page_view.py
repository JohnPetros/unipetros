from flask import render_template

from core.use_cases.admin import get_professor_details_page_data

from infra.forms.professor_form import ProfessorForm

from infra.auth import get_auth_user, login_checker, role_checker


@login_checker
@role_checker("admin")
def get_professor_details_page_view(professor_id) -> str:
    user = get_auth_user()

    data = get_professor_details_page_data.execute(professor_id)
    professor = data["professor"]
    related_professors = data["related_professors"]

    professor_form = ProfessorForm(professor=professor)

    return render_template(
        "pages/admin/professor_details/index.html",
        user=user,
        professor=professor,
        related_professors=related_professors,
        professor_form=professor_form,
    )
