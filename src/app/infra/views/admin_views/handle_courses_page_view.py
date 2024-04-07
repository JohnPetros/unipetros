from flask import render_template, request

from core.use_cases.admin import (
    get_courses_page_data,
    create_course,
)

from infra.auth import get_auth_user, login_checker, role_checker


@login_checker
@role_checker("admin")
def handle_courses_page_view() -> str:
    user = get_auth_user()

    courses_page_data = get_courses_page_data.execute()

    courses = courses_page_data["courses"]
    course_form = courses_page_data["course_form"]

    if request.method == "POST" and course_form.validate_on_submit():
        updated_courses = create_course.execute(course_form.data)
        courses = updated_courses

    return render_template(
        "pages/admin/courses/index.html",
        user=user,
        courses=courses,
        course_form=course_form,
    )
