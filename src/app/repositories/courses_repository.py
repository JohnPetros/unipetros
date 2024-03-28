from typing import List, Dict

from database import mysql

from entities.course import Course
from entities.subject import Subject


class CoursesRepository:
    def get_courses(self) -> List[Course]:
        courses = mysql.query(
            sql="""
                SELECT 
                    C.*, 
                    GROUP_CONCAT(S.id) AS subjects_ids, 
                    GROUP_CONCAT(S.name) AS subjects_names
                FROM courses AS C
                JOIN courses_subjects AS CS ON CS.course_id = C.id 
                JOIN subjects AS S ON CS.subject_id = S.id
                GROUP BY C.id
                """,
            is_single=False,
        )

        if len(courses) == 0:
            return []

        return list(map(self.__get_course_entity, courses))

    def create_course(self, course: Course) -> None:
        mysql.mutate(
            sql="""
                INSERT INTO courses (id, name, description) 
                VALUES (%s, %s, %s)
                """,
            params=[course.id, course.name, course.description],
        )

        if len(course.subjects) > 0:
            for subject in course.subjects:
                mysql.mutate(
                    sql="""
                        INSERT INTO courses_subjects (course_id, subject_id) 
                        VALUES (%s, %s)
                        """,
                    params=[course.id, subject.id],
                )

    def __get_course_entity(self, course: Dict) -> Course:
        if course["subjects_ids"] and course["subjects_names"]:
            subjects_ids = course["subjects_ids"].split(",")
            subjects_names = course["subjects_names"].split(",")

        subjects = []

        for index, subject_id in enumerate(subjects_ids):
            subjects.append(Subject(id=subject_id, name=subjects_names[index]))

        return Course(
            id=course["id"],
            name=course["name"],
            description=course["description"],
            subjects=subjects,
        )
