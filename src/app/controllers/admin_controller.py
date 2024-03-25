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

from providers.image_processor_provider import ImageProcessorProvider

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

    def handle_professor_page(self, professor_id: str) -> ProfessorModel:
        if not isinstance(professor_id, str):
            raise Error("Professor id is None", 400)

        professor = professors_repository.get_professor_by_id(professor_id)

        if not isinstance(professor, ProfessorModel):
            raise Error("Professor not found", 404)

        return professor
