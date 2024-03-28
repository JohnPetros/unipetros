from typing import Union, Dict, List

from database import mysql

from entities.subject import Subject
from entities.professor import Professor

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

        return Professor(professor, professor["id"])

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

    def __get_professor_entity(self, professor: Dict) -> Professor:
        if professor["subjects_ids"] and professor["subjects_names"]:
            subjects_ids = professor["subjects_ids"].split(",")
            subjects_names = professor["subjects_names"].split(",")

        subjects = []

        for index, subject_id in enumerate(subjects_ids):
            subjects.append(Subject(id=subject_id, name=subjects_names[index]))

        professor_model = Professor(
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
