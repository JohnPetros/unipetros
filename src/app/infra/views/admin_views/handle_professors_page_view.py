from flask import render_template, request

from core.use_cases.admin import get_filtered_professors, create_professor

from infra.auth import get_auth_user, login_checker, role_checker
from infra.repositories import subjects_repository
from infra.forms.professor_form import ProfessorForm


@login_checker
@role_checker("admin")
def handle_professors_page_view() -> str:
    user = get_auth_user()

    search = request.args.get("search")
    subjects_ids = request.args.getlist("subjects_ids")
    page = request.args.get("page", 1)

    try:
        professors = get_filtered_professors.excute(
            name_or_email=search, subjects_ids=subjects_ids, page_number=page
        )

        subjects = subjects_repository.get_subjects()

        subjects_checkbox_group = [(subject.id, subject.name) for subject in subjects]

        professor_form = ProfessorForm()
        professor_form.subjects.choices = subjects_checkbox_group

        if request.method == "POST" and professor_form.validate_on_submit():
            create_professor.execute(professor_form.data)
            professors = get_filtered_professors.excute()
    except Exception:
        pass

    return render_template(
        "pages/admin/professors/index.html",
        user=user,
        search_value=search,
        subjects_checkbox_group=subjects_checkbox_group,
        professor_form=professor_form,
        professors=professors,
    )
