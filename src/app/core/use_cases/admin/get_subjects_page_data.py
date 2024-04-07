from infra.repositories import subjects_repository
from infra.forms.subject_form import SubjectForm
from infra.utils.error import Error


class GetSubjectsPageData:
    def execute(self):
        try:
            subjects = subjects_repository.get_subjects()
            subject_form = SubjectForm()

            return {
                "subjects": subjects,
                "subject_form": subject_form,
            }
        except Exception as exception:
            raise Error(
                "Não foi possível buscar os dados de disciplinas"
            ) from exception
