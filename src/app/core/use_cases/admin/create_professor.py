from typing import Dict

from core.entities.professor import Professor
from core.entities.subject import Subject
from core.commons.email import Email
from core.commons.avatar import Avatar


from infra.auth import hash_password
from infra.repositories import professors_repository
from infra.utils.error import Error


class CreateProfessor:
    def execute(self, professor: Dict):
        try:
            email = Email(professor["email"])
            email.validate(role="professor")

            avatar = Avatar(professor["avatar"])
            avatar_image_name = avatar.get_image_name()

            new_professor = Professor(
                email=email.get_value(),
                password=hash_password(professor["password"]),
                name=professor["name"],
                phone=professor["phone"],
                gender=professor["gender"],
                birthdate=professor["birthdate"],
                avatar=avatar_image_name,
                subjects=[Subject(id=subject) for subject in professor["subjects"]],
            )

            professors_repository.create_professor(new_professor)

            professors = professors_repository.get_professors()
            return professors

        except Error as error:
            raise error
