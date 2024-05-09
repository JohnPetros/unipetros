from typing import Dict

from core.entities.course import Course
from core.entities.subject import Subject

from infra.repositories import courses_repository
from infra.utils.error import Error


class CreateCourse:
    def execute(self, course: Dict):
        try:
            new_course = Course(
                name=course["name"],
                description=course["description"],
                subjects=[Subject(id=subject) for subject in course["subjects"]],
            )

            courses_repository.create_course(new_course)

            return courses_repository.get_courses()

        except Exception as exception:
            print(exception)
            raise Error("Não foi possível cadastrar curso", 500) from exception
