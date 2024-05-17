from core.entities.professor import Professor
from core.entities.subject import Subject
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

            professor = Professor(
                id=professor_id,
                name=request["name"],
                email=request["email"],
                password=hash_password(request["password"]),
                avatar=request["avatar"],
                phone=request["phone"],
                gender=request["gender"],
                birthdate=request["birthdate"],
                subjects=[
                    Subject(id=subject_id) for subject_id in request["subjects_ids"]
                ],
            )

            professors_repository.update_professor(professor)
            updated_professor = professors_repository.get_professor_by_id(professor_id)

            return updated_professor
        except Error as error:
            raise error
