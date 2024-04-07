from typing import Union, Dict, List

from infra.database import mysql

from core.entities.subject import Subject
from core.entities.professor import Professor

from .users_repository import UsersRepository


class ProfessorsRepository(UsersRepository):
    def get_professor_by_id(self, id: str) -> Union[Professor, None]:
        professor = mysql.query(
            sql="SELECT * FROM professors WHERE id = %s", params=[id]
        )

        if not professor:
            return None

        return self.__get_professor_entity(professor)

    def get_professor_by_email(self, email: str) -> Union[Professor, None]:
        professor = mysql.query(
            sql="SELECT * FROM professors WHERE email = %s", params=[email]
        )

        if not professor:
            return None

        return self.__get_professor_entity(professor)

    def get_professors_count_by_subject(self) -> int:
        result = mysql.query(
            sql="""
            SELECT 
                COUNT(P.id) AS professors_count,
                S.name
            FROM professors AS P
            LEFT JOIN professors_subjects AS PS ON PS.professor_id = P.id 
            LEFT JOIN subjects AS S ON PS.subject_id = S.id
            GROUP BY S.name
            """,
            is_single=False,
        )

        return int(result["count"])

    def get_professors(self) -> List[Professor]:
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

        professors = list(map(self.__get_professor_entity, professors))

        return professors

    def get_professors_count(self):
        result = mysql.query(
            sql="SELECT COUNT(id) AS count FROM professors",
            is_single=True,
        )

        return int(result["count"])

    def create_professor(self, professor: Professor) -> None:
        mysql.mutate(
            sql="""
                INSERT INTO professors (id, name, email, password, phone, birthdate, gender, avatar) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """,
            params=[
                professor.id,
                professor.name,
                professor.email,
                professor.password,
                professor.phone,
                professor.birthdate,
                professor.gender,
                professor.avatar,
            ],
        )

        if len(professor.subjects) > 0:
            for subject in professor.subjects:
                mysql.mutate(
                    sql="""
                        INSERT INTO professors_subjects (professor_id, subject_id)
                        VALUE (%s, %s)
                        """,
                    params=[
                        professor.id,
                        subject.id,
                    ],
                )

    def __get_professor_entity(self, professor_data: Dict) -> Professor:
        subjects_ids = []
        subjects_names = []

        if "subjects_ids" in professor_data and "subjects_names" in professor_data:
            subjects_ids = professor_data["subjects_ids"].split(",")
            subjects_names = professor_data["subjects_names"].split(",")

        subjects = []

        for index, subject_id in enumerate(subjects_ids):
            subjects.append(Subject(id=subject_id, name=subjects_names[index]))

        professor = Professor(
            id=professor_data["id"],
            email=professor_data["email"],
            name=professor_data["name"],
            password=professor_data["password"],
            avatar=professor_data["avatar"],
            birthdate=professor_data["birthdate"],
            gender=professor_data["gender"],
            subjects=subjects,
        )

        if not self.should_get_password:
            del professor.password

        return professor
