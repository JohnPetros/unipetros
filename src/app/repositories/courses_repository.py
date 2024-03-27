from typing import Dict

from database import mysql

from models.course_model import CourseModel


class CoursesRepository:
    def get_courses(self):
        courses = mysql.query(sql="SELECT * FROM courses", is_single=False)

        if len(courses) == 0:
            return []

        return list(map(self.__get_course_model, courses))

    def __get_course_model(self, course: Dict):
        return CourseModel(
            id=course["id"],
            name=course["name"],
            description=course["description"],
        )
