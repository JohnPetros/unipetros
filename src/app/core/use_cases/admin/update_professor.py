from core.commons.email import Email
from core.entities.professor import Professor
from core.entities.subject import Subject
from core.commons.avatar import Avatar

from infra.utils.error import Error
from infra.repositories import professors_repository
from infra.auth import hash_password


class UpdateProfessor:
    def execute(self, request):
        try:
            professor_id = request["id"]

            current_professor = professors_repository.get_professor_by_id(professor_id)

            if not isinstance(current_professor, Professor):
                raise Error("Professor não encontrado", 404)

            email = Email(request["email"])
            is_email = email.validate(
                role="professor", exceptions=[current_professor.email]
            )

            if not is_email:
                raise Error("E-mail não válido")

            avatar = Avatar(
                request["avatar"], default_image_name=current_professor.avatar
            )
            avatar_image_name = avatar.get_image_name()

            if avatar_image_name == current_professor.avatar:
                avatar_image_name = current_professor.avatar

            professor = Professor(
                id=professor_id,
                name=request["name"],
                email=email.get_value(),
                password=hash_password(request["password"]),
                avatar=avatar_image_name,
                phone=request["phone"],
                gender=request["gender"],
                birthdate=request["birthdate"],
                subjects=[
                    Subject(id=subject_id) for subject_id in request["subjects_ids"]
                ],
            )

            professors = professors_repository.get_professors_by_subjects_ids(
                [subject.id for subject in professor.subjects]
            )

            related_professors = [
                professor for professor in professors if professor.id != professor_id
            ]

            professors_repository.update_professor(professor)
            updated_professor = professors_repository.get_professor_by_id(professor_id)

            return {
                "updated_professor": updated_professor,
                "related_professors": related_professors,
            }
        except Error as error:
            raise error
