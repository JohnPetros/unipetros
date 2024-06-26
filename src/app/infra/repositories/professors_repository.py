from typing import Union, Dict, List


from core.entities.subject import Subject
from core.entities.professor import Professor

from core.constants.pagination_limit import PAGINATION_LIMIT

from infra.database import mysql

from .users_repository import UsersRepository


class ProfessorsRepository(UsersRepository):
    def get_professor_by_id(self, id: str) -> Union[Professor, None]:
        row = mysql.query(
            sql="""
            SELECT 
                P.*, 
                GROUP_CONCAT(S.id) AS subjects_ids, 
                GROUP_CONCAT(S.name) AS subjects_names
            FROM professors AS P
            LEFT JOIN professors_subjects AS PS ON PS.professor_id = P.id 
            LEFT JOIN subjects AS S ON PS.subject_id = S.id
            WHERE P.id = %s
            """,
            params=[id],
            is_single=True,
        )

        if not row:
            return None

        return self.__get_professor_entity(row)

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

    def get_professors(self):
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

    def get_professors_by_subjects_ids(self, ids: list[str]):
        subjects_ids = ",".join([f"'{id}'" for id in ids])

        professors = mysql.query(
            sql=f"""
                SELECT
                    P.*,
                    GROUP_CONCAT(S.id) AS subjects_ids,
                    GROUP_CONCAT(S.name) AS subjects_names
                FROM professors AS P
                LEFT JOIN professors_subjects AS PS ON PS.professor_id = P.id
                LEFT JOIN subjects AS S ON PS.subject_id = S.id
                WHERE S.id IN ({subjects_ids})
                GROUP BY P.id
                """,
            is_single=False,
        )

        if len(professors) == 0:
            return []

        professors = list(map(self.__get_professor_entity, professors))

        return professors

    def get_filtered_professors(
        self,
        name: str = None,
        email: str = None,
        subjects_ids: List[str] = [],
        page_number: int = 1,
        gender: str = "all",
    ) -> List[Professor]:
        filters = []

        if name:
            filters.append(f" P.name LIKE '%{name}%' ")

        if email:
            filters.append(f" P.email LIKE '%{email}%' ")

        if len(subjects_ids) > 0:
            ids = ",".join(list(map(lambda id: f"'{id}'", subjects_ids)))
            filters.append(f" S.id IN ({ids}) ")

        if gender != "all":
            filters.append(f" P.gender = '{gender}' ")

        if len(filters) > 0:
            filters = "WHERE" + "AND".join(filters)
        else:
            filters = ""

        offset = (int(page_number) - 1) * PAGINATION_LIMIT

        professors = mysql.query(
            sql=f"""
                SELECT 
                    P.*, 
                    GROUP_CONCAT(S.id) AS subjects_ids, 
                    GROUP_CONCAT(S.name) AS subjects_names
                FROM professors AS P
                LEFT JOIN professors_subjects AS PS ON PS.professor_id = P.id 
                LEFT JOIN subjects AS S ON PS.subject_id = S.id
                {filters}
                GROUP BY P.id
                LIMIT {PAGINATION_LIMIT}
                OFFSET {offset}
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
                INSERT INTO professors 
                (id, name, email, password, phone, birthdate, gender, avatar) 
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

    def update_professor(self, professor: Professor):
        mysql.mutate(
            "DELETE FROM professors_subjects WHERE professor_id = %s",
            params=[professor.id],
        )

        for subject in professor.subjects:
            mysql.mutate(
                sql="""
                    INSERT INTO professors_subjects 
                    (professor_id, subject_id) VALUES
                    (%s, %s)   
                    """,
                params=[professor.id, subject.id],
            )

        mysql.mutate(
            sql="""
                UPDATE professors SET 
                    name = %s,
                    email = %s,
                    password = %s,
                    phone = %s,
                    birthdate = %s,
                    gender = %s,
                    avatar = %s
                WHERE id = %s
                """,
            params=[
                professor.name,
                professor.email,
                professor.password,
                professor.phone,
                professor.birthdate,
                professor.gender,
                professor.avatar,
                professor.id,
            ],
        )

    def delete_professor_by_id(self, professor_id: str):
        mysql.mutate(
            sql="DELETE FROM professors WHERE id = %s",
            params=[professor_id],
        )

    def __get_professor_entity(self, professor_data: Dict) -> Professor:
        subjects_ids = []
        subjects_names = []

        if (
            "subjects_ids" in professor_data
            and professor_data["subjects_ids"] is not None
            and "subjects_names" in professor_data
            and professor_data["subjects_names"] is not None
        ):
            subjects_ids = professor_data["subjects_ids"].split(",")
            subjects_names = professor_data["subjects_names"].split(",")

        subjects = []

        for index, subject_id in enumerate(subjects_ids):
            subjects.append(Subject(id=subject_id, name=subjects_names[index]))

        avatar = professor_data["avatar"]

        professor = Professor(
            id=professor_data["id"],
            email=professor_data["email"],
            name=professor_data["name"],
            password=professor_data["password"],
            phone=professor_data["phone"],
            avatar=avatar if avatar is not None else "default-avatar.png",
            birthdate=professor_data["birthdate"],
            gender=professor_data["gender"],
            subjects=subjects,
        )

        if not self.should_get_password:
            del professor.password

        return professor
