from typing import Dict

from core.entities.subject import Subject

from infra.repositories import subjects_repository
from infra.utils.error import Error


class CreateSubject:
    def execute(self, subject: Dict):
        try:
            new_subject = Subject(
                name=subject["name"], description=subject["description"]
            )

            subjects_repository.create_subject(new_subject)

            return subjects_repository.get_subjects()

        except Exception as exception:
            print(exception)
            raise Error("Não foi possível cadastratar disciplina", 500) from exception
