USERS_MAP = {
    "nome": "name",
    "e-mail": "email",
    "telefone": "phone",
    "senha": "password",
    "data de nascimento": "birthdate",
    "gênero": "gender",
}

CSV_COLUMNS_MAP = {
    "professors": {**USERS_MAP, "disciplinas": "subjects"},
    "students": {**USERS_MAP, "curso": "course"},
}
