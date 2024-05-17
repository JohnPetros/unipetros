from infra.repositories import professors_repository

from core.constants.folders import FOLDERS
from core.entities.professor import Professor

from infra.utils.error import Error
from infra.utils.file import File


class DeleteProfessors:
    def execute(self, professors_ids: list[str]):
        try:
            for id in professors_ids:
                professor = professors_repository.get_professor_by_id(id)

                if not isinstance(professor, Professor):
                    raise Error("Professor não encontrado")

                avatar_file = File(FOLDERS["uploaded_images"], professor.avatar)
                avatar_file.delete()

                professors_repository.delete_professor_by_id(id)
        except Error as error:
            raise error
