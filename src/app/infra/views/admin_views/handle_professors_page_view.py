from flask import render_template, request

from core.use_cases.admin import get_filtered_professors
from infra.utils.error import Error

from infra.auth import get_auth_user, login_checker, role_checker
from infra.repositories import subjects_repository
from infra.forms.professor_form import ProfessorForm


@login_checker
@role_checker("admin")
def handle_professors_page_view() -> str:
    user = get_auth_user()

    search = request.args.get("search")
    gender = request.args.get("gender", "all")
    subjects_ids = request.args.getlist("subjects_ids[]")
    page = request.args.get("page", 1)

    try:
        professors, pages_count = get_filtered_professors.excute(
            name_or_email=search,
            subjects_ids=subjects_ids,
            gender=gender,
            page_number=page,
        )

        subjects = subjects_repository.get_subjects()

        subjects_checkbox_group = [(subject.id, subject.name) for subject in subjects]

        professor_form = ProfessorForm()
        professor_form.subjects.choices = subjects_checkbox_group

        return render_template(
            "pages/admin/professors/index.html",
            user=user,
            search_value=search,
            gender=gender,
            subjects_checkbox_group=subjects_checkbox_group,
            selected_subjects_ids=subjects_ids,
            professor_form=professor_form,
            professors=professors,
            pages_count=pages_count,
        )
    except Error:
        return render_template(
            "pages/admin/professors/index.html",
            user=user,
            search_value=search,
            gender=gender,
            subjects_checkbox_group=subjects_checkbox_group,
            professor_form=professor_form,
            professors=professors,
            pages_count=pages_count,
        )
