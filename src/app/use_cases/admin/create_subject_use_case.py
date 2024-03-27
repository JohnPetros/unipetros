from typing import Dict

from models.subject_model import SubjectModel

from repositories import subjects_repository

from utils.error import Error


class CreateSubjectUseCase:
    def execute(self, subject: Dict):
        try:
            new_subject = SubjectModel(
                name=subject["name"], description=subject["description"]
            )

            subjects_repository.create_subject(new_subject)

            return subjects_repository.get_subjects()

        except Exception as exception:
            print(exception)
            raise Error("Não foi possível cadastratar disciplina", 500) from exception
