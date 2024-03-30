from typing import List, Dict

from database import mysql

from entities.course import Course
from entities.subject import Subject


class CoursesRepository:
    def get_courses(self) -> List[Course]:
        courses = mysql.query(
            sql="""
                SELECT C.*, COUNT(S.id) AS students_count
                FROM courses AS C
                LEFT JOIN students AS S ON S.course_id = C.id
                GROUP BY C.id
                """,
            is_single=False,
        )

        if len(courses) == 0:
            return []

        return list(map(self.__get_course_entity, courses))

    def get_courses_ordered_by_students_count(self) -> List[Dict]:
        courses = mysql.query(
            sql="""
               SELECT C.*, COUNT(S.id) AS students_count
               FROM courses AS C
               LEFT JOIN students AS S ON S.course_id = C.id
               GROUP BY C.id
               LIMIT 4
                """,
            is_single=False,
        )

        if len(courses) == 0:
            return []

        return list(map(self.__get_course_entity_with_students_count, courses))

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

    def __get_course_entity(self, course_data: Dict) -> Course:
        subjects_ids = []
        subjects_names = []

        if "subjects_ids" in course_data and "subjects_names" in course_data:
            subjects_ids = course_data["subjects_ids"].split(",")
            subjects_names = course_data["subjects_names"].split(",")

        subjects = []

        for index, subject_id in enumerate(subjects_ids):
            subjects.append(Subject(id=subject_id, name=subjects_names[index]))

        return Course(
            id=course_data["id"],
            name=course_data["name"],
            description=course_data["description"],
            subjects=subjects,
        )

    def __get_course_entity_with_students_count(self, course_data: Dict) -> Dict:
        course = self.__get_course_entity(course_data)

        return {"course": course, "students_count": course_data["students_count"]}
