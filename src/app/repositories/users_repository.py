from typing import Union
from models.user_model import UserModel
from database import mysql


class UsersRepository:
    def get_user_by_id(self, id: str) -> Union[UserModel, None]:
        user = mysql.query(sql="SELECT * FROM users WHERE id= %s", params=[id])

        print(id)

        if not user:
            return None

        return UserModel(user, user["id"])

    def get_user_by_email(self, email: str) -> Union[UserModel, None]:
        user = mysql.query(sql="SELECT * FROM users WHERE email= %s", params=[email])

        if not user:
            return None

        return UserModel(user, user["id"])

    def save(self, user: UserModel) -> None:
        mysql.mutate(
            sql="""
            INSERT INTO users (id, email, name, password, role) 
            VALUES (%s, %s, %s, %s, %s)
            """,
            params=[user.id, user.email, user.name, user.password, user.role],
        )
