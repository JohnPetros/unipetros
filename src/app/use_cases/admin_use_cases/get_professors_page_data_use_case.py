from typing import Dict, Union, List

from entities.professor import Professor

from repositories import subjects_repository, professors_repository

from forms.professor_form import ProfessorForm

from utils.error import Error


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
