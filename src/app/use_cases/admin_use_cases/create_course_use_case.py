from typing import Dict

from entities.course import Course
from entities.subject import Subject

from repositories import courses_repository

from utils.error import Error


class CreateCourseUseCase:
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
