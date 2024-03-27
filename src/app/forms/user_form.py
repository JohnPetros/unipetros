from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, RadioField, DateField
from wtforms.validators import DataRequired, Email, Length, EqualTo, Regexp


class UserForm(FlaskForm):
    name = StringField(
        "Nome completo",
        validators=[DataRequired(message="Nome é obrigatório"), Length(3)],
        render_kw={"autofocus": True},
    )
    email = StringField(
        "E-mail", validators=[DataRequired(message="E-mail é obrigatório"), Email()]
    )
    password = PasswordField(
        "Senha",
        validators=[
            DataRequired(message="Senha é obrigatório"),
            Length(min=6, max=20, message="Senha conter ter entre 6 a 20 caracteres"),
        ],
    )
    password_confirmation = PasswordField(
        "Confirme sua senha",
        validators=[
            DataRequired(message="Confirmação de senha é obrigatório"),
            EqualTo("password", message="As senhas devem ser iguais"),
        ],
    )
    phone = StringField(
        "Telefone",
        validators=[
            DataRequired(message="Telefone é obrigatório"),
            Regexp(regex="^-?\d+$", message="Telefone inválido"),
        ],
    )
    gender = RadioField(
        "Gênero",
        choices=[
            ("male", "Masculino"),
            ("female", "Feminino"),
        ],
        default="male",
        validators=[DataRequired(message="Gênero é obrigatório")],
    )
    birthdate = DateField(
        "Data de nascimento",
        validators=[DataRequired(message="Data de nascimento é obrigatório")],
    )
    avatar = FileField(
        "Avatar",
        validators=[FileAllowed(["jpg", "png"])],
        render_kw={"data-avatar-input": "input"},
    )
