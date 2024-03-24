from typing import Union

from database import mysql

from models.student_model import StudentModel


class StudentsRepository:
    def get_student_by_id(self, id: str) -> Union[StudentModel, None]:
        student = mysql.query(sql="SELECT * FROM students WHERE id= %s", params=[id])

        if not student:
            return None

        return StudentModel(student, student["id"])

    def get_student_by_email(self, email: str) -> Union[StudentModel, None]:
        student = mysql.query(
            sql="SELECT * FROM students WHERE email= %s", params=[email]
        )

        if not student:
            return None

        return StudentModel(student, student["id"])
