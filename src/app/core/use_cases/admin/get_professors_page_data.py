from typing import Dict, Union, List

from core.entities.professor import Professor

from infra.repositories import subjects_repository
from infra.forms.professor_form import ProfessorForm
from infra.utils.error import Error


class GetProfessorsPageData:
    def execute(self) -> Dict[str, Union[List[Professor], ProfessorForm]]:
        try:
            subjects = subjects_repository.get_subjects()

            professors_form = ProfessorForm()
            professors_form.subjects.choices = [
                (subject.id, subject.name) for subject in subjects
            ]

            return {
                "professor_form": professors_form,
            }

        except Exception as exception:
            return Error(exception, 500)
