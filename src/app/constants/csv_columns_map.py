USERS_MAP = {
    "Nome": "name",
    "E-mail": "email",
    "Telefone": "phone",
    "Senha": "password",
    "Data de nascimento": "birthdate",
    "Gênero": "gender",
}

CSV_COLUMNS_MAP = {
    "professors": {**USERS_MAP, "Disciplinas": "subjects"},
}
