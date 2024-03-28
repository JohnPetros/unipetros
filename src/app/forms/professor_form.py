from wtforms.validators import DataRequired

from wtforms import SubmitField
from .user_form import UserForm
from .fields.multi_checkbox_field import MultiCheckboxField


class ProfessorForm(UserForm):
    subjects = MultiCheckboxField("Disciplinas")
    submit_button = SubmitField("Adicionar professor", validators=[DataRequired()])
