from typing import Union

from models.user_model import UserModel
from repositories.users_repository import UsersRepository
import auth

users_repository = UsersRepository()


class UsersController:
    def handle_login(self, email: str, password: str) -> Union[UserModel, None]:
        user = users_repository.get_user_by_email(email)

        if not user or not auth.check_password(user.password, password):
            return None

        return user
