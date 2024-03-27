from typing import Union, Dict

from database import mysql

from models.student_model import StudentModel
from models.course_model import CourseModel
from .users_repository import UsersRepository


class StudentsRepository(UsersRepository):
    def get_student_by_id(self, id: str) -> Union[StudentModel, None]:
        student = mysql.query(sql="SELECT * FROM students WHERE id = %s", params=[id])

        if not student:
            return None

        return self.__get_student_model(student)

    def get_student_by_email(self, email: str) -> Union[StudentModel, None]:
        student = mysql.query(
            sql="SELECT * FROM students WHERE email = %s", params=[email]
        )

        if not student:
            return None

        return self.__get_student_model(student)

    def get_students(self):
        students = mysql.query(
            sql="""
            SELECT 
                S.*, 
                C.name AS course_name
            FROM students AS S
            JOIN courses AS C ON C.id = S.course_id
            """,
            is_single=False,
        )

        if len(students) == 0:
            return []

        return list(map(self.__get_student_model, students))

    def __get_student_model(self, student: Dict):
        course = CourseModel(name=student["course_name"])

        return StudentModel(
            id=student["id"],
            email=student["email"],
            name=student["name"],
            password=student["password"],
            avatar=student["avatar"],
            birthdate=student["birthdate"],
            gender="masculino" if student["gender"] == "male" else "feminino",
            course=course,
        )
