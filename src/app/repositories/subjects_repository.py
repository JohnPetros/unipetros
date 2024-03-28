from typing import Dict, List

from database import mysql

from entities.subject import Subject


class SubjectsRepository:
    def get_subjects(self) -> List[Subject]:
        subjects = mysql.query(sql="SELECT * FROM subjects", is_single=False)

        return list(map(self.__get_subject_entity, subjects))

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
