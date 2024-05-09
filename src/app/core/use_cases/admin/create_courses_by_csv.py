from typing import List, Dict

from werkzeug.datastructures import FileStorage

from core.entities.course import Course
from core.entities.subject import Subject

from core.constants.csv_columns_map import CSV_COLUMNS_MAP
from core.constants.gender_map import GENDER_MAP

from infra.repositories import courses_repository, subjects_repository
from infra.auth import hash_password
from infra.providers import data_analyser_provider
from infra.utils.error import Error


class CreateCoursesByCSV:
    def execute(self, csv: FileStorage) -> List[Course]:
        self.__validate_csv(csv)

        extension = self.__get_csv_extension(csv)

        records = self.__get_records(csv, extension)

        courses = []

        all_subjects = subjects_repository.get_subjects()

        for record in records:
            new_course = self.__format_course_record(record, all_subjects)

            courses.append(Course(**new_course))

        for course in courses:
            courses_repository.create_course(course)

        return courses_repository.get_courses()

    def __validate_csv(self, csv: FileStorage):
        if not isinstance(csv, FileStorage):
            raise Error("Arquivo de cursos precisa ser um arquivo csv")

        extension = self.__get_csv_extension(csv)

        if extension not in ["xlsx", "csv"]:
            raise Error(
                "Arquivo contendo os cursos precisam ser must um arquivo csv ou excel válido"
            )

    def __get_records(self, csv: FileStorage, extension: str):
        data_analyser_provider.analyse(csv)

        if extension == "csv":
            data_analyser_provider.read_csv()
        else:
            data_analyser_provider.read_excel()

        records = data_analyser_provider.convert_to_list_of_records()

        return records

    def __get_csv_extension(self, csv: FileStorage) -> str:
        return csv.filename.split(".")[1]

    def __format_course_record(self, record: Dict, all_subjects: List[Subject]) -> Dict:
        course = {}

        for key, value in record.items():
            if key.lower() in CSV_COLUMNS_MAP["courses"]:
                course_attribute = CSV_COLUMNS_MAP["courses"][key.lower()]

                match course_attribute:
                    case "subjects":
                        value = self.__get_courses_subjects(value, all_subjects)
                    case "password":
                        value = hash_password(str(value))
                    case "gender":
                        value = GENDER_MAP[value.lower()]

                course[course_attribute] = value

        course["avatar"] = "default-avatar.png"
        return course

    def __get_courses_subjects(self, value: str, all_subjects: List[Subject]):
        subjects_names = value.split(",")
        course_subjects = []

        for subject_name in subjects_names:
            course_subject = self.__get_subject_by_name(all_subjects, subject_name)

            if course_subject:
                course_subjects.append(course_subject)

        return course_subjects

    def __get_subject_by_name(
        self, subjects: List[Subject], subject_name
    ) -> Subject | None:
        for subject in subjects:
            if subject.name.lower() == subject_name.lower():
                return subject

        return None
