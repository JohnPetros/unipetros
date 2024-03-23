from flask import Flask
from flask_login import LoginManager, login_user, current_user
from flask_bcrypt import Bcrypt

from models.user_model import UserModel
from repositories.users_repository import UsersRepository
from .auth_user import AuthUser

login_manager = LoginManager()
bcrypt = Bcrypt()


def get_user(id: str) -> UserModel:
    users_repository = UsersRepository()
    return users_repository.get_user_by_id(id)


def login(user: UserModel) -> None:
    return login_user(user, remember=False)


def hash_password(password: str) -> bytes:
    return bcrypt.generate_password_hash(password)


def check_password(password_hash: str, password) -> bool:
    return bcrypt.check_password_hash(password_hash, password)


def get_auth_user() -> AuthUser:
    return current_user


def init_auth(app: Flask) -> None:
    login_manager.init_app(app)
    login_manager.user_loader(get_user)

    bcrypt.init_app(app)
