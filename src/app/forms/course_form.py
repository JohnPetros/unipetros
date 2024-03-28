from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import SubmitField, StringField, TextAreaField

from .fields.multi_checkbox_field import MultiCheckboxField


class CourseForm(FlaskForm):
    name = StringField("Nome")
    description = TextAreaField("Descrição")
    subjects = MultiCheckboxField("Disciplinas")
    submit_button = SubmitField("Adicionar curso", validators=[DataRequired()])
