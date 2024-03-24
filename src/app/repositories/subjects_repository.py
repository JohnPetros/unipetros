from typing import Dict, List

from database import mysql

from models.subject_model import SubjectModel


class SubjectsRepository:
    def get_subjects(self) -> List[SubjectModel]:
        subjects = mysql.query(sql="SELECT * FROM subjects", is_single=False)

        return map(self.__get_subject_model, subjects)

    def __get_subject_model(self, subject: Dict) -> SubjectModel:
        return SubjectModel(id=subject["id"], name=subject["name"])
