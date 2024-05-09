from infra.repositories import professors_repository

from infra.utils.error import Error


class DeleteProfessors:
    def execute(self, professors_ids: list[str]):
        try:
            for id in professors_ids:
                professors_repository.delete_professor_by_id(id)
        except Error as error:
            raise error
