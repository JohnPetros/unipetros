from typing import Callable
from functools import wraps

from flask import Flask
from flask_login import (
    LoginManager,
    login_user,
    logout_user,
    login_required,
    current_user,
)
from flask_bcrypt import Bcrypt

from models.user_model import UserModel
from repositories.users_repository import UsersRepository
from .auth_user import AuthUser

login_manager = LoginManager()
bcrypt = Bcrypt()


def get_user(id: str) -> UserModel:
    users_repository = UsersRepository()
    user = users_repository.get_user_by_id(id)
    return AuthUser(user)


def login(user: UserModel, should_remember_user) -> None:
    return login_user(user, remember=should_remember_user)


def hash_password(password: str) -> bytes:
    return bcrypt.generate_password_hash(password)


def check_password(password_hash: str, password) -> bool:
    return bcrypt.check_password_hash(password_hash, password)


def login_checker(view: Callable) -> Callable:
    @wraps(view)
    def check_login(*args, **kwargs):
        return login_required(view)(*args, **kwargs)

    return check_login


def logout():
    return logout_user()


def get_auth_user() -> AuthUser:
    return current_user


def init_auth(app: Flask) -> None:
    login_manager.init_app(app)
    login_manager.user_loader(get_user)
    login_manager.login_view = "auth_views.login"
    login_manager.login_message = "Por favor, faça seu login antes"
    login_manager.login_message_category = "warn"

    bcrypt.init_app(app)
