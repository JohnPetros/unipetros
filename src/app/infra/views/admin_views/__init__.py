from flask import Blueprint

from .get_analytics_page_view import get_analytics_page_view

from .create_professors_by_csv_view import create_professors_by_csv_view
from .create_professor_by_form_view import create_professor_by_form_view
from .get_professor_details_page_view import get_professor_details_page_view
from .get_filtered_professors_view import get_filtered_professors_view
from .handle_professors_page_view import handle_professors_page_view
from .delete_professors_view import delete_professors_view
from .update_professor_view import update_professor_view
from .get_professors_csv_view import get_professors_csv_view

from .handle_students_page_view import handle_students_page_view
from .create_students_by_csv_view import create_students_by_csv_view

from .handle_subjects_page_view import handle_subjects_page_view
from .create_subjects_by_csv_view import create_subjects_by_csv_view

from .handle_courses_page_view import handle_courses_page_view
from .create_courses_by_csv_view import create_courses_by_csv_view

admin_views = Blueprint("admin_views", __name__)

route = admin_views.add_url_rule

route(rule="/dashboard/analytics", view_func=get_analytics_page_view)

route(
    rule="/dashboard/professors",
    view_func=handle_professors_page_view,
    methods=["GET"],
)

route(
    rule="/dashboard/professors/filter",
    view_func=get_filtered_professors_view,
    methods=["GET"],
)

route(
    rule="/dashboard/professors/csv",
    view_func=get_professors_csv_view,
    methods=["GET"],
)

route(
    rule="/dashboard/professors/csv",
    view_func=create_professors_by_csv_view,
    methods=["POST"],
)

route(
    rule="/dashboard/professors/form",
    view_func=create_professor_by_form_view,
    methods=["POST"],
)

route(
    rule="/dashboard/professors/delete",
    view_func=delete_professors_view,
    methods=["DELETE"],
)

route(
    rule="/dashboard/professors/<id>",
    view_func=update_professor_view,
    methods=["PUT"],
)

route(
    rule="/dashboard/professors/<professor_id>",
    view_func=get_professor_details_page_view,
    methods=["GET", "POST"],
)

route(
    rule="/dashboard/students",
    view_func=handle_students_page_view,
    methods=["GET", "POST"],
)
route(
    rule="/dashboard/students/csv",
    view_func=create_students_by_csv_view,
    methods=["POST"],
)

route(
    rule="/dashboard/subjects/csv",
    view_func=create_subjects_by_csv_view,
    methods=["POST"],
)

route(
    rule="/dashboard/subjects",
    view_func=handle_subjects_page_view,
    methods=["GET", "POST"],
)

route(
    rule="/dashboard/courses",
    view_func=handle_courses_page_view,
    methods=["GET", "POST"],
)

route(
    rule="/dashboard/courses/csv",
    view_func=create_courses_by_csv_view,
    methods=["POST"],
)
