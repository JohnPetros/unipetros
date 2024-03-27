from typing import Dict

from database import mysql

from entities.course import Course


class CoursesRepository:
    def get_courses(self):
        courses = mysql.query(sql="SELECT * FROM courses", is_single=False)

        if len(courses) == 0:
            return []

        return list(map(self.__get_course_entity, courses))

    def __get_course_entity(self, course: Dict):
        return Course(
            id=course["id"],
            name=course["name"],
            description=course["description"],
        )
