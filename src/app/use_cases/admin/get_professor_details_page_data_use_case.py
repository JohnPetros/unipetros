from typing import Dict, Union, List

from entities.professor import Professor

from repositories import professors_repository

from forms.professor_form import ProfessorForm

from utils.error import Error


class GetProfessorDetailsPageDataUseCase:
    def execute(
        self, professor_id: str
    ) -> Dict[str, Union[List[Professor], ProfessorForm]]:
        try:
            if not isinstance(professor_id, str):
                raise Error("Id do Professor não fonercido", 500)

            professor = professors_repository.get_professor_by_id(professor_id)

            if not isinstance(professor, Professor):
                raise Error("Professor não encontrado", 404)

            return professor

        except Exception as exception:
            return Error(exception, 500)
