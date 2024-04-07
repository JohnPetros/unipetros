from flask import render_template, request

from core.use_cases.admin import get_filtered_professors

from infra.auth import get_auth_user, login_checker, role_checker
from infra.repositories import subjects_repository
from infra.forms.professor_form import ProfessorForm


@login_checker
@role_checker("admin")
def get_professors_page_view() -> str:
    user = get_auth_user()

    search = request.args.get("search")
    professors = get_filtered_professors.excute(name_or_email=search, subjects_ids=[])

    subjects = subjects_repository.get_subjects()

    professor_form = ProfessorForm()
    professor_form.subjects.choices = [
        (subject.id, subject.name) for subject in subjects
    ]

    return render_template(
        "pages/admin/professors/index.html",
        user=user,
        professor_form=professor_form,
        professors=professors,
    )
