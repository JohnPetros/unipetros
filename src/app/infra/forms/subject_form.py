from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import SubmitField, StringField, TextAreaField


class SubjectForm(FlaskForm):
    name = StringField("Nome")
    description = TextAreaField("Descrição")
    submit_button = SubmitField("Adicionar professor", validators=[DataRequired()])
