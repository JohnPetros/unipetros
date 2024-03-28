from flask import render_template, request

from auth import get_auth_user, login_checker, role_checker

from use_cases.admin_use_cases import (
    get_subjects_page_data_use_case,
    create_subject_use_case,
)


@login_checker
@role_checker("admin")
def create_students_by_csv_view() -> str:
    user = get_auth_user()

    subjects_page_data = get_subjects_page_data_use_case.execute()

    subjects = subjects_page_data["subjects"]
    subject_form = subjects_page_data["professor_form"]

    if request.method == "POST" and subject_form.validate_on_submit():
        updated_subjects = create_subject_use_case.execute(subject_form.data)
        subjects = updated_subjects

    return render_template(
        "pages/admin/subjects/index.html",
        user=user,
        subjects=subjects,
        subject_form=subject_form,
    )
