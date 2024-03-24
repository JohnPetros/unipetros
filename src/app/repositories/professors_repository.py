from typing import Union, Dict, List

from database import mysql

from models.subject_model import SubjectModel
from models.professor_model import ProfessorModel
from .users_repository import UsersRepository


class ProfessorsRepository(UsersRepository):
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
                SELECT 
                    P.*, 
                    GROUP_CONCAT(S.id) AS subjects_ids, 
                    GROUP_CONCAT(S.name) AS subjects_names
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

    def create_professor(self, professor: ProfessorModel) -> None:
        mysql.mutate(
            sql="""
                INSERT INTO professors (id, name, email, password, phone, birthdate, gender, avatar) 
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """,
            params=[
                professor.id,
                professor.name,
                professor.email,
                professor.phone,
                professor.gender,
                professor.avatar,
            ],
        )

    def __get_professor_model(self, professor: Dict) -> ProfessorModel:
        subjects_ids = professor["subjects_ids"].split(",")
        subjects_names = professor["subjects_names"].split(",")
        subjects = []

        for index, subject_id in enumerate(subjects_ids):
            subjects.append(SubjectModel(id=subject_id, name=subjects_names[index]))

        professor_model = ProfessorModel(
            id=professor["id"],
            email=professor["email"],
            name=professor["name"],
            password=professor["password"],
            avatar=professor["avatar"],
            birthdate=professor["birthdate"],
            gender="masculino" if professor["gender"] == "male" else "feminino",
            subjects=subjects,
        )

        del professor_model.password
        return professor_model
