from typing import List, Dict

from werkzeug.datastructures import FileStorage

from models.professor_model import ProfessorModel
from models.subject_model import SubjectModel

from repositories.professors_repository import ProfessorsRepository
from repositories.subjects_repository import SubjectsRepository

from providers.data_analyser_provider import DataAnalyserProvider

from utils.error import Error

from constants.csv_columns_map import CSV_COLUMNS_MAP

professors_repository = ProfessorsRepository()
subjects_repository = SubjectsRepository()
data_analyser_provider = DataAnalyserProvider()


class CreateProfessorsByCSVController:
    def execute(self, csv: FileStorage):
        self.__validate_csv(csv)

        extension = self.__get_csv_extension(csv)

        records = self.__get_records(csv, extension)

        professors = []

        for record in records:
            new_professor = self.__format_professor_record(record)

            professors.append(ProfessorModel(**new_professor))

        for professor in professors:
            professors_repository.create_professor(professor)

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
        return csv.filename.split(".")[0]

    def __format_professor_record(self, record: Dict):
        all_subjects = subjects_repository.get_subjects()
        professor = {}

        for key, value in record.items():
            if key in CSV_COLUMNS_MAP["professors"]:
                professor_attribute = CSV_COLUMNS_MAP["users"][key]
                professor_subjects = []

                if professor_attribute == "subjects":
                    subjects_names = value.split(",")

                    for subject_name in subjects_names:
                        professor_subject = self.__get_subject_by_name(
                            all_subjects, subject_name
                        )

                        if professor_subject:
                            professor_subjects.append(professor_subject)

                professor[professor_attribute] = value

        return professor

    def __get_subject_by_name(
        self, subjects: List[SubjectModel], subject_name
    ) -> SubjectModel | None:
        for subject in subjects:
            if subject.name == subject_name:
                return subject
        return None
