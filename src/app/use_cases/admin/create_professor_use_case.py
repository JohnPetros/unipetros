from typing import Dict, Any

from uuid import uuid4 as generate_random_name
from werkzeug.datastructures import FileStorage

from entities.professor import Professor
from entities.subject import Subject

from repositories import professors_repository

from auth import hash_password

from utils.error import Error
from utils.file import File

from constants.folders import FOLDERS

from providers.image_processor_provider import ImageProcessorProvider


class CreateProfessorUseCase:
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

        except Exception as exception:
            return Error(exception)

    def __validate_professor_email(self, email: str) -> bool:
        professor_already_exists = professors_repository.get_professor_by_email(email)

        if professor_already_exists:
            return Error("Professor já existente com esse e-mail", 400)

        return True

    def __get_avatar_image(self, avatar: Any):
        image_name = "default.png"

        if isinstance(avatar, FileStorage):
            _, extension = avatar.filename.split(".")

            image_name = f"{generate_random_name()}.{extension}"

            file = File(FOLDERS["tmp"], image_name)

            avatar.save(file.path)

            image_processor = ImageProcessorProvider()
            image_processor.register(file.path)
            image_processor.resize(400, 400)
            image_processor.save()

            return image_name

        return image_name