from typing import Dict

from utils.error import Error

from repositories import subjects_repository


class CreateSubjectUseCase:
    def execute(self, subject: Dict):
        try:
            subjects_repository.create_subject(subject)

            return subjects_repository.get_subjects()

        except Exception as exception:
            raise Error("Não foi possível cadastratar disciplina", 500) from exception
