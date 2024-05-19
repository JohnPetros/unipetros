from random import randint

from core.constants.csv_columns_map import CSV_COLUMNS_MAP
from core.constants.folders import FOLDERS
from core.constants.gender_map import GENDER_MAP

from infra.repositories import professors_repository
from infra.providers.data_analyser_provider import DataAnalyserProvider
from infra.utils.error import Error


class CreateProfessorsCsv:
    def execute(self):
        try:
            data = self.__get_data()

            csv_name = f"professors-{randint(1, 100)}.xlsx"
            tmp_folder = FOLDERS["tmp"]

            data_analyser_provider = DataAnalyserProvider()
            data_analyser_provider.analyse(data)
            data_analyser_provider.convert_to_excel(tmp_folder, csv_name)

            return {
                "folder": tmp_folder,
                "filename": csv_name,
            }
        except Exception:
            raise Error()

    def __get_data(self):
        professors = professors_repository.get_professors()

        data = {
            column: []
            for column in CSV_COLUMNS_MAP["professors"].keys()
            if column != "senha"
        }

        genders = dict(zip(GENDER_MAP.values(), GENDER_MAP.keys()))

        for column, attribute in CSV_COLUMNS_MAP["professors"].items():
            for professor in professors:
                value = getattr(professor, attribute)

                if attribute == "password":
                    continue

                if attribute == "subjects" and len(value) > 0:
                    data[column].append(",".join([subject.name for subject in value]))
                    continue

                if attribute == "gender":
                    data[column].append(genders[value])
                    continue

                data[column].append(value)

        return data
