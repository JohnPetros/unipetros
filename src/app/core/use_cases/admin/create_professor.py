from typing import Dict, Any

from uuid import uuid4 as generate_random_name
from werkzeug.datastructures import FileStorage

from core.entities.professor import Professor
from core.entities.subject import Subject

from core.constants.folders import FOLDERS

from infra.auth import hash_password
from infra.repositories import professors_repository
from infra.utils.error import Error
from infra.utils.file import File
from infra.providers.image_processor_provider import ImageProcessorProvider


class CreateProfessor:
    def execute(self, professor: Dict):
        try:
            self.__validate_professor_email(professor["email"])

            avatar = professor["avatar"]

            image_name = self.__get_avatar_image(avatar)

            new_professor = Professor(
                email=professor["email"],
                name=professor["name"],
                password=hash_password(professor["password"]),
                phone=professor["phone"],
                gender=professor["gender"],
                birthdate=professor["birthdate"],
                avatar=image_name,
                subjects=[Subject(id=subject) for subject in professor["subjects"]],
            )

            professors_repository.create_professor(new_professor)

            professors = professors_repository.get_professors()
            return professors

        except Error as error:
            print(error)
            raise Error(ui_message=error)

    def __validate_professor_email(self, email: str) -> bool:
        professor_already_exists = professors_repository.get_professor_by_email(email)

        if professor_already_exists:
            raise Error("Professor já existente com esse e-mail")

        return True

    def __get_avatar_image(self, avatar: Any):
        image_name = "default-avatar.png"

        if isinstance(avatar, FileStorage):
            _, extension = avatar.filename.split(".")

            image_name = f"{generate_random_name()}.{extension}"

            file = File(FOLDERS["uploaded_images"], image_name)

            avatar.save(file.path)

            image_processor = ImageProcessorProvider()
            image_processor.register(file.path)
            image_processor.resize(400, 400)
            image_processor.save()

            return image_name

        return image_name
