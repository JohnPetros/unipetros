from flask import render_template

from core.use_cases.admin import get_analytics_page_data

from infra.auth import get_auth_user, login_checker, role_checker


@login_checker
@role_checker("admin")
def get_analytics_page_view() -> str:
    user = get_auth_user()

    data = get_analytics_page_data.execute()

    return render_template(
        "pages/admin/analytics/index.html",
        user=user,
        total_professors=data["total_professors"],
        total_students=data["total_students"],
        total_subjects=data["total_subjects"],
        total_students_by_gender=data["total_students_by_gender"],
        total_posts_by_category=data["total_posts_by_category"],
        popular_courses=data["popular_courses"],
        last_enrolled_students=data["last_enrolled_students"],
        students_activity_by_range_days=data["students_activity_by_range_days"],
        professors_count_by_gender_and_subject=data[
            "professors_count_by_gender_and_subject"
        ],
    )
