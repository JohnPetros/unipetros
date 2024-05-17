from wtforms.validators import DataRequired
from wtforms import SubmitField

from .user_form import UserForm
from .fields.multi_checkbox_field import MultiCheckboxField

from core.entities.professor import Professor
from infra.repositories import subjects_repository


class ProfessorForm(UserForm):
    def __init__(self, formdata=None, professor=None, **kwargs):
        super().__init__(formdata, **kwargs)

        subjects = subjects_repository.get_subjects()
        self.subjects.choices = [(subject.id, subject.name) for subject in subjects]

        if isinstance(professor, Professor):
            self.name.data = professor.name
            self.email.data = professor.email
            self.phone.data = professor.phone
            self.avatar.data = professor.avatar
            self.birthdate.data = professor.birthdate
            self.gender.data = professor.gender
            self.checked_subjects_ids = [subject.id for subject in professor.subjects]

    subjects = MultiCheckboxField("Disciplinas", name="subjects[]")
    checked_subjects_ids = []
    submit_button = SubmitField("Adicionar professor", validators=[DataRequired()])
