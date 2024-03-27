from repositories import subjects_repository
from forms.subject_form import SubjectForm
from utils.error import Error


class GetSubjectsPageDataUseCase:
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
