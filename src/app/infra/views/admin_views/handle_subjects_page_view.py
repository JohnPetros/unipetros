from flask import render_template, request

from core.use_cases.admin import get_subjects_page_data, create_subject

from infra.auth import get_auth_user, login_checker, role_checker


@login_checker
@role_checker("admin")
def handle_subjects_page_view() -> str:
    user = get_auth_user()

    subjects_page_data = get_subjects_page_data.execute()

    subjects = subjects_page_data["subjects"]
    subject_form = subjects_page_data["subject_form"]

    if request.method == "POST" and subject_form.validate_on_submit():
        updated_subjects = create_subject.execute(subject_form.data)
        subjects = updated_subjects

    return render_template(
        "pages/admin/subjects/index.html",
        user=user,
        subjects=subjects,
        subject_form=subject_form,
    )
