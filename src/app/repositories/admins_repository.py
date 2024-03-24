from typing import Dict

from database import mysql

from models.admin_model import AdminModel
from .users_repository import UsersRepository


class AdminsRepository(UsersRepository):
    def get_admin_by_id(self, id: str) -> AdminModel | None:
        admin = mysql.query(sql="SELECT * FROM admins WHERE id = %s", params=[id])

        if not admin:
            return None

        return self.__get_admin_model(admin)

    def get_admin_by_email(self, email: str) -> AdminModel | None:
        admin = mysql.query(sql="SELECT * FROM admins WHERE email = %s", params=[email])

        if not admin:
            return None

        return self.__get_admin_model(admin)

    def save(self, admin: AdminModel) -> None:
        mysql.mutate(
            sql="""
            INSERT INTO admins (id, email, name, password, role) 
            VALUES (%s, %s, %s, %s, %s)
            """,
            params=[admin.id, admin.email, admin.name, admin.password, admin.role],
        )

    def __get_admin_model(self, admin: Dict) -> AdminModel:
        return AdminModel(
            id=admin["id"],
            email=admin["email"],
            name=admin["name"],
            avatar=admin["avatar"],
            password=admin["password"],
            created_by="John Petros",
        )
