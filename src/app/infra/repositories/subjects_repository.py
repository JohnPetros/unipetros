from typing import Dict, List

from infra.database import mysql

from core.entities.subject import Subject


class SubjectsRepository:
    def get_subjects(self) -> List[Subject]:
        subjects = mysql.query(sql="SELECT * FROM subjects", is_single=False)

        return list(map(self.__get_subject_entity, subjects))

    def get_subjects_count(self) -> int:
        result = mysql.query(
            sql="SELECT COUNT(id) AS count FROM subjects",
            is_single=True,
        )

        return int(result["count"])

    def create_subject(self, subject: Subject):
        mysql.mutate(
            sql="""
                INSERT INTO subjects (id, name, description) 
                VALUES (%s, %s, %s)
                """,
            params=[subject.id, subject.name, subject.description],
        )

    def __get_subject_entity(self, subject: Dict) -> Subject:
        return Subject(
            id=subject["id"], name=subject["name"], description=subject["description"]
        )
