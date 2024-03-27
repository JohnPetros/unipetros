from typing import Dict

from entities.student import Student

from repositories import students_repository

from utils.error import Error


class CreateStudentUseCase:
    def execute(self, student_data: Dict):
        try:
            new_student = Student(
                name=student_data["name"], description=student_data["description"]
            )

            students_repository.create_student(new_student)

            return students_repository.get_students()

        except Exception as exception:
            print(exception)
            raise Error("Não foi possível cadastratar disciplina", 500) from exception
