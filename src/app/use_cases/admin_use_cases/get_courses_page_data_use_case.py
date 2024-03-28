from typing import Dict, Union, List

from entities.course import Course

from repositories import courses_repository, subjects_repository

from forms.course_form import CourseForm

from utils.error import Error


class GetCoursesPageDataUseCase:
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
