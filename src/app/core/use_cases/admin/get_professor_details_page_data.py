from typing import Dict, Union, List

from core.entities.professor import Professor

from infra.repositories import professors_repository
from infra.forms.professor_form import ProfessorForm
from infra.utils.error import Error


class GetProfessorDetailsPageData:
    def execute(
        self, professor_id: str
    ) -> Dict[str, Union[List[Professor], ProfessorForm]]:
        try:
            if not isinstance(professor_id, str):
                raise Error("Id do Professor não fonercido", 500)

            professor = professors_repository.get_professor_by_id(professor_id)

            if not professor or not isinstance(professor, Professor):
                raise Error("Professor não encontrado", 404)

            related_professors = professors_repository.get_professors_by_subjects_ids(
                [subject.id for subject in professor.subjects]
            )

            return {"professor": professor, "related_professors": related_professors}

        except Error as error:
            return error
