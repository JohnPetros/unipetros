from typing import Dict, Union, List

from entities.professor import Professor

from repositories.professors_repository import ProfessorsRepository
from repositories.subjects_repository import SubjectsRepository

from forms.professor_form import ProfessorForm

from utils.error import Error

professors_repository = ProfessorsRepository()
subjects_repository = SubjectsRepository()


class GetProfessorsPageDataUseCase:
    def execute(self) -> Dict[str, Union[List[Professor], ProfessorForm]]:
        try:
            professors = professors_repository.get_professors()
            subjects = subjects_repository.get_subjects()

            professors_form = ProfessorForm()
            professors_form.subjects.choices = [
                (subject.id, subject.name) for subject in subjects
            ]

            return {
                "professors": professors,
                "professor_form": professors_form,
            }

        except Exception as exception:
            return Error(exception, 500)
