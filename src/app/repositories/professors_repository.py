from typing import Union, Dict, List

from database import mysql

from models.professor_model import ProfessorModel


class ProfessorsRepository:
    def __init__(self, should_get_password=False) -> None:
        self.should_get_password = should_get_password

    def __get_professor_model(self, professor: Dict):
        professor_model = ProfessorModel(
            id=professor["id"],
            email=professor["email"],
            name=professor["name"],
            password=professor["password"],
            avatar=professor["avatar"],
            birthdate=professor["birthdate"],
            subjects=professor["subjects_names"].split(","),
        )

        del professor_model.password
        return professor_model

    def get_professor_by_id(self, id: str) -> Union[ProfessorModel, None]:
        professor = mysql.query(
            sql="SELECT * FROM professors WHERE id = %s", params=[id]
        )

        if not professor:
            return None

        return self.__get_professor_model(professor)

    def get_professor_by_email(self, email: str) -> Union[ProfessorModel, None]:
        professor = mysql.query(
            sql="SELECT * FROM professors WHERE email = %s", params=[email]
        )

        if not professor:
            return None

        return ProfessorModel(professor, professor["id"])

    def get_professors(self) -> List[ProfessorModel]:
        professors = mysql.query(
            sql="""
                SELECT P.*, GROUP_CONCAT(S.name) AS subject_names
                FROM professors AS P
                LEFT JOIN professors_subjects AS PS ON PS.professor_id = P.id 
                LEFT JOIN subjects AS S ON PS.subject_id = S.id
                GROUP BY P.id
                """,
            is_single=False,
        )

        if len(professors) == 0:
            return []

        professors = list(map(self.__get_professor_model, professors))

        return professors
