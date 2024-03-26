from typing import Dict, Union, List

from models.professor_model import ProfessorModel

from repositories.professors_repository import ProfessorsRepository
from repositories.subjects_repository import SubjectsRepository

from forms.professor_form import ProfessorForm

from utils.error import Error

professors_repository = ProfessorsRepository()
subjects_repository = SubjectsRepository()


class GetProfessorPageDataController:
    def execute(
        self, professor_id: str
    ) -> Dict[str, Union[List[ProfessorModel], ProfessorForm]]:
        try:
            if not isinstance(professor_id, str):
                raise Error("Id do Professor não fonercido", 500)

            professor = professors_repository.get_professor_by_id(professor_id)

            if not isinstance(professor, ProfessorModel):
                raise Error("Professor não encontrado", 404)

            return professor

        except Exception as exception:
            return Error(exception, 500)
