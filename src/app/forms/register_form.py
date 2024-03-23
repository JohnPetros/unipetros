from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class RegisterForm(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    password = PasswordField("Senha", validators=[Length(6, 20)])
    password_confirmation = PasswordField(
        "Confirme sua senha", validators=[EqualTo("password")]
    )
    submit_button = SubmitField("Cadastrar-se")
