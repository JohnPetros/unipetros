from typing import Union, List, Dict

from database import mysql

from entities.student import Student
from entities.course import Course

from .users_repository import UsersRepository


class StudentsRepository(UsersRepository):
    def get_student_by_id(self, id: str) -> Union[Student, None]:
        student = mysql.query(sql="SELECT * FROM students WHERE id = %s", params=[id])

        if not student:
            return None

        return self.__get_student_model(student)

    def get_student_by_email(self, email: str) -> Union[Student, None]:
        student = mysql.query(
            sql="SELECT * FROM students WHERE email = %s", params=[email]
        )

        if not student:
            return None

        return self.__get_student_model(student)

    def get_students(self) -> List[Student]:
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

    def get_students_count(self) -> int:
        result = mysql.query(
            sql="SELECT COUNT(id) AS count FROM students",
            is_single=True,
        )

        return int(result["count"])

    def get_students_count_by_gender(self) -> int:
        return mysql.query(
            sql="""
            SELECT gender, COUNT(gender) AS count
            FROM students
            GROUP BY gender
            """,
            is_single=False,
        )

    def create_student(self, student: Student) -> None:
        mysql.mutate(
            sql="""
                INSERT INTO students 
                (id, name, email, password, phone, birthdate, gender, avatar, course_id) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """,
            params=[
                student.id,
                student.name,
                student.email,
                student.password,
                student.phone,
                student.birthdate,
                student.gender,
                student.avatar,
                student.course.id,
            ],
        )

    def __get_student_model(self, student_data: Dict):
        course = Course(name=student_data["course_name"])

        student = Student(
            id=student_data["id"],
            email=student_data["email"],
            name=student_data["name"],
            password=student_data["password"],
            avatar=student_data["avatar"],
            birthdate=student_data["birthdate"],
            gender="masculino" if student_data["gender"] == "male" else "feminino",
            course=course,
        )

        if not self.should_get_password:
            del student.password

        return student
