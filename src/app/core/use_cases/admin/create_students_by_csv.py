from typing import List, Dict

from werkzeug.datastructures import FileStorage

from core.entities.student import Student
from core.entities.course import Course

from core.constants.csv_columns_map import CSV_COLUMNS_MAP
from core.constants.gender_map import GENDER_MAP

from infra.repositories import students_repository, courses_repository
from infra.providers import data_analyser_provider
from infra.utils.error import Error
from infra.auth import hash_password


class CreateStudentsByCSV:
    def execute(self, csv: FileStorage) -> List[Student]:
        try:
            self.__validate_csv(csv)

            extension = self.__get_csv_extension(csv)

            records = self.__get_records(csv, extension)

            students: List[Student] = []

            all_courses = courses_repository.get_courses()

            for record in records:
                new_student = self.__format_student_record(record, all_courses)

                students.append(Student(**new_student))

            for student in students:
                students_repository.create_student(student)

            return students_repository.get_students()
        except Exception as exception:
            raise Error(
                ui_message="Não foi possível usar os dados de estudantes desse arquivo csv",
                error_message=exception,
            ) from exception

    def __validate_csv(self, csv: FileStorage) -> None:
        if not isinstance(csv, FileStorage):
            raise Error("Arquivo de estudantes precisa ser um arquivo csv")

        extension = self.__get_csv_extension(csv)

        if extension not in ["xlsx", "csv"]:
            raise Error(
                "Arquivo contendo os students precisam ser must um arquivo csv ou excel válido"
            )

    def __get_records(self, csv: FileStorage, extension: str) -> List[Dict]:
        data_analyser_provider.analyse(csv)

        if extension == "csv":
            data_analyser_provider.read_csv()
        else:
            data_analyser_provider.read_excel()

        records = data_analyser_provider.convert_to_list_of_records()

        return records

    def __get_csv_extension(self, csv: FileStorage) -> str:
        return csv.filename.split(".")[1]

    def __format_student_record(self, record: Dict, all_courses: List[Course]) -> None:
        student = {}

        for key, value in record.items():
            if key.lower() in CSV_COLUMNS_MAP["students"]:
                student_attribute = CSV_COLUMNS_MAP["students"][key.lower()]

                match student_attribute:
                    case "course":
                        value = self.__get_student_course(value, all_courses)
                    case "password":
                        value = hash_password(str(value))
                    case "gender":
                        value = GENDER_MAP[value.lower()]

                student[student_attribute] = value

        student["avatar"] = "default-avatar.png"
        return student

    def __get_student_course(
        self, course_name: str, all_courses: List[Course]
    ) -> Course | None:
        student_course: Course = None

        for course in all_courses:
            if course.name.lower() == course_name.lower():
                student_course = course

        return student_course
