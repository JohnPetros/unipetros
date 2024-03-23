from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class LoginForm(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    password = PasswordField("Senha", validators=[Length(6, 20)])
    remember_me = BooleanField("Lembre-se de mim")
    submit_button = SubmitField("Login", validators=[DataRequired()])
