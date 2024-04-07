from typing import Dict, Union, List

from core.entities.course import Course

from infra.repositories import courses_repository, subjects_repository
from infra.forms.course_form import CourseForm
from infra.utils.error import Error


class GetCoursesPageData:
    def execute(self) -> Dict[str, Union[List[Course], CourseForm]]:
        try:
            courses = courses_repository.get_courses()
            subjects = subjects_repository.get_subjects()

            course_form = CourseForm()
            course_form.subjects.choices = [
                (course.id, course.name) for course in subjects
            ]

            return {
                "courses": courses,
                "course_form": course_form,
            }

        except Exception as exception:
            return Error(exception, 500)
