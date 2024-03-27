from typing import Dict, Union, List

from uuid import uuid4 as generate_random_name
from werkzeug.datastructures import FileStorage

from models.professor_model import ProfessorModel
from models.subject_model import SubjectModel

from repositories.professors_repository import ProfessorsRepository
from repositories.subjects_repository import SubjectsRepository

from auth import hash_password

from forms.professor_form import ProfessorForm

from utils.error import Error
from utils.file import File

from constants.folders import FOLDERS
from constants.csv_columns_map import CSV_COLUMNS_MAP

from providers.image_processor_provider import ImageProcessorProvider
from providers.data_analyser_provider import DataAnalyserProvider

professors_repository = ProfessorsRepository()
subjects_repository = SubjectsRepository()


class AdminController:
    def handle_professors_page(
        self,
    ) -> Dict[str, Union[List[ProfessorModel], ProfessorForm]]:
        try:
            professors = professors_repository.get_professors()
            subjects = subjects_repository.get_subjects()

            professors_form = ProfessorForm()
            professors_form.subjects.choices = [
                (subject.id, subject.name) for subject in subjects
            ]

            return {
                "professors": professors,
                "professor_form": professors_form,
            }
        except Exception as exception:
            return Error(exception, 500)

    def handle_new_professor(self, professor: Dict) -> None:
        try:
            professor_already_exists = professors_repository.get_professor_by_email(
                professor["email"]
            )

            if professor_already_exists:
                return Error("Professor já existente com esse e-mail", 400)

            avatar = professor["avatar"]
            if isinstance(avatar, FileStorage):
                _, extension = professor["avatar"].filename.split(".")

                image_name = f"{generate_random_name()}.{extension}"

                file = File(FOLDERS["tmp"], image_name)
                avatar.save(file.path)

                image_processor = ImageProcessorProvider()
                image_processor.register(file.path)
                image_processor.resize(400, 400)
                image_processor.save()
            else:
                image_name = "default.png"

            new_professor = ProfessorModel(
                email=professor["email"],
                name=professor["name"],
                password=hash_password(professor["password"]),
                phone=professor["phone"],
                gender=professor["gender"],
                birthdate=professor["birthdate"],
                avatar=image_name,
                subjects=[
                    SubjectModel(id=subject) for subject in professor["subjects"]
                ],
            )

            professors_repository.create_professor(new_professor)

            professors = professors_repository.get_professors()
            return professors
        except Error as error:
            return Error(error)

    def handle_professors_csv(self, csv: FileStorage):
        if not isinstance(csv, FileStorage):
            raise Error("Professors csv must be a file")

        extension = csv.filename.split(".")[1]
        print(csv.filename)
        print(extension)

        if extension not in ["xlsx", "csv"]:
            raise Error("Professors csv must be a csv or excel file")

        data_analyser_provider = DataAnalyserProvider()
        data_analyser_provider.analyse(csv)

        if extension == "csv":
            data_analyser_provider.read_csv()
        else:
            data_analyser_provider.read_excel()

        records = data_analyser_provider.convert_to_list_of_records()

        subjects = subjects_repository.get_subjects()

        professors = []
        for record in records:
            new_professor = {}
            for key, value in record.items():
                if key in CSV_COLUMNS_MAP["professors"]:
                    professor_attribute = CSV_COLUMNS_MAP["users"][key]
                    if professor_attribute == "subjects":
                        subjects_names = value.split(",")
                        for subject_name in subjects_names:
                            is_subject = lambda subject: subject.name == subject_name

                            professor_subject = next(
                                filter(
                                    is_subject,
                                    subjects,
                                ),
                                None,
                            )

                    new_professor[professor_attribute] = value

            professors.append(ProfessorModel(**new_professor))

        for professor in professors:
            professors_repository.create_professor(professor)

        print(professors)

    def handle_professor_page(self, professor_id: str) -> ProfessorModel:
        if not isinstance(professor_id, str):
            raise Error("Professor id is None", 400)

        professor = professors_repository.get_professor_by_id(professor_id)

        if not isinstance(professor, ProfessorModel):
            raise Error("Professor not found", 404)

        return professor
