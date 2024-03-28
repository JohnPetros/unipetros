from typing import Dict, Any

from uuid import uuid4 as generate_random_name

from werkzeug.datastructures import FileStorage

from auth import hash_password

from entities.student import Student
from entities.course import Course

from repositories import students_repository

from constants.folders import FOLDERS

from utils.error import Error
from utils.file import File

from providers import image_processor_provider


class CreateStudentUseCase:
    def execute(self, student_data: Dict):
        try:
            self.__validate_student_email(student_data["email"])

            image_name = self.__get_avatar_image(student_data["avatar"])

            new_student = Student(
                email=student_data["email"],
                name=student_data["name"],
                password=hash_password(student_data["password"]),
                phone=student_data["phone"],
                gender=student_data["gender"],
                birthdate=student_data["birthdate"],
                avatar=image_name,
                course=Course(id=student_data["course"]),
            )

            students_repository.create_student(new_student)

            return students_repository.get_students()

        except Exception as exception:
            print(exception)
            raise Error("Não foi possível cadastratar aluno", 500) from exception

    def __validate_student_email(self, email: str) -> bool:
        professor_already_exists = students_repository.get_student_by_email(email)

        if professor_already_exists:
            return Error("Aluno já existente com esse e-mail", 400)

        return True

    def __get_avatar_image(self, avatar: Any):
        image_name = "default.png"

        if isinstance(avatar, FileStorage):
            _, extension = avatar.filename.split(".")

            image_name = f"{generate_random_name()}.{extension}"

            file = File(FOLDERS["tmp"], image_name)

            avatar.save(file.path)

            image_processor_provider.register(file.path)
            image_processor_provider.resize(400, 400)
            image_processor_provider.save()

            return image_name

        return image_name
