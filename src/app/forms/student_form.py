from wtforms.validators import DataRequired
from wtforms import RadioField, SubmitField

from .user_form import UserForm


class StudentForm(UserForm):
    course = RadioField("Curso")
    submit_button = SubmitField(
        "Adicionar estudante", validators=[DataRequired(message="Curso é obrigatório")]
    )
