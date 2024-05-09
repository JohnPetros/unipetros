from typing import Dict, Any

from uuid import uuid4 as generate_random_name

from werkzeug.datastructures import FileStorage

from core.entities.student import Student
from core.entities.course import Course

from core.constants.folders import FOLDERS

from infra.auth import hash_password
from infra.repositories import students_repository

from infra.providers import image_processor_provider

from infra.utils.error import Error
from infra.utils.file import File


class CreateStudent:
    def execute(self, student_data: Dict):
        try:
            print("student_data", student_data)
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
        image_name = "default-avatar.png"

        if isinstance(avatar, FileStorage):
            _, extension = avatar.filename.split(".")

            image_name = f"{generate_random_name()}.{extension}"

            file = File(FOLDERS["uploaded_images"], image_name)

            avatar.save(file.path)

            image_processor_provider.register(file.path)
            image_processor_provider.resize(320, 320)
            image_processor_provider.save()

            return image_name

        return image_name
