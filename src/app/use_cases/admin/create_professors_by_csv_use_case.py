from typing import List, Dict

from werkzeug.datastructures import FileStorage

from entities.professor import Professor
from entities.subject import Subject

from repositories import professors_repository, subjects_repository

from providers import data_analyser_provider

from auth import hash_password

from utils.error import Error

from constants.csv_columns_map import CSV_COLUMNS_MAP
from constants.gender_map import GENDER_MAP


class CreateProfessorsByCSVUseCase:
    def execute(self, csv: FileStorage) -> List[Professor]:
        self.__validate_csv(csv)

        extension = self.__get_csv_extension(csv)

        records = self.__get_records(csv, extension)

        professors = []

        for record in records:
            new_professor = self.__format_professor_record(record)

            professors.append(Professor(**new_professor))

        for professor in professors:
            professors_repository.create_professor(professor)

        return professors_repository.get_professors()

    def __validate_csv(self, csv: FileStorage):
        if not isinstance(csv, FileStorage):
            raise Error("Professors csv must be a file")

        extension = self.__get_csv_extension(csv)

        if extension not in ["xlsx", "csv"]:
            raise Error("Professors csv must be a csv or excel file")

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

    def __format_professor_record(self, record: Dict):
        all_subjects = subjects_repository.get_subjects()
        professor = {}

        for key, value in record.items():
            if key in CSV_COLUMNS_MAP["professors"]:
                professor_attribute = CSV_COLUMNS_MAP["professors"][key]

                match professor_attribute:
                    case "subjects":
                        value = self.__get_professors_subjects(value, all_subjects)
                    case "password":
                        value = hash_password(str(value))
                    case "gender":
                        value = GENDER_MAP[value.lower()]

                professor[professor_attribute] = value

        professor["avatar"] = "default-avatar.png"
        return professor

    def __get_professors_subjects(self, value: str, all_subjects: List[Subject]):
        subjects_names = value.split(",")
        professor_subjects = []

        for subject_name in subjects_names:
            professor_subject = self.__get_subject_by_name(all_subjects, subject_name)

            if professor_subject:
                professor_subjects.append(professor_subject)

        return professor_subjects

    def __get_subject_by_name(
        self, subjects: List[Subject], subject_name
    ) -> Subject | None:
        for subject in subjects:
            if subject.name.lower() == subject_name.lower():
                return subject

        return None
