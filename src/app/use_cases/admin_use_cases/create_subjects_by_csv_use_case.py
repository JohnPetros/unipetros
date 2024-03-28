from typing import List, Dict

from werkzeug.datastructures import FileStorage

from entities.subject import Subject

from repositories import subjects_repository

from providers import data_analyser_provider

from utils.error import Error

from constants.csv_columns_map import CSV_COLUMNS_MAP


class CreateSubjectsByCSVUseCase:
    def execute(self, csv: FileStorage) -> List[Subject]:
        try:
            self.__validate_csv(csv)

            extension = self.__get_csv_extension(csv)

            records = self.__get_records(csv, extension)

            subjects: List[Subject] = []

            for record in records:
                new_subject = self.__format_subject_record(record)

                subjects.append(Subject(**new_subject))

            for subject in subjects:
                subjects_repository.create_subject(subject)

            return subjects_repository.get_subjects()
        except Exception as exception:
            print(exception)
            raise Error(
                "Não foi possível usar os dados de disciplinas desse arquivo csv"
            ) from exception

    def __validate_csv(self, csv: FileStorage) -> None:
        if not isinstance(csv, FileStorage):
            raise Error("Arquivo de disciplinas precisa ser um arquivo csv")

        extension = self.__get_csv_extension(csv)

        if extension not in ["xlsx", "csv"]:
            raise Error(
                "Arquivo contendo os subjects precisam ser must um arquivo csv ou excel válido"
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

    def __format_subject_record(self, record: Dict) -> None:
        subject = {}

        for key, value in record.items():
            if key.lower() in CSV_COLUMNS_MAP["subjects"]:
                subject_attribute = CSV_COLUMNS_MAP["subjects"][key.lower()]

                subject[subject_attribute] = value

        subject["avatar"] = "default-avatar.png"
        return subject
