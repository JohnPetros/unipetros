from typing import Callable, Literal, Union
from functools import wraps
from dataclasses import asdict

from flask import Flask, redirect, url_for, flash

from flask_login import (
    LoginManager,
    login_user,
    logout_user,
    login_required,
    current_user,
)
from flask_bcrypt import Bcrypt

from core.entities.admin import Admin
from core.entities.professor import Professor
from core.entities.student import Student

from infra.repositories import (
    admins_repository,
    professors_repository,
    students_repository,
)

from .auth_user import AuthUser

login_manager = LoginManager()
bcrypt = Bcrypt()


def get_user(stored_user_data) -> AuthUser:
    id = stored_user_data["id"]
    role = stored_user_data["role"]

    match role:
        case "admin":
            user = admins_repository.get_admin_by_id(id)
        case "professor":
            user = professors_repository.get_professor_by_id(id)
        case "student":
            user = students_repository.get_student_by_id(id)

    if user is None:
        return AuthUser(is_active=False)

    return AuthUser(role=role, **asdict(user))


def login(user: Union[Admin, Professor, Student], should_remember_user) -> None:
    return login_user(user, remember=should_remember_user)


def hash_password(password: str) -> bytes:
    return bcrypt.generate_password_hash(password).decode("utf-8")


def check_password(password_hash: str, password) -> bool:
    return bcrypt.check_password_hash(password_hash, password)


def login_checker(view: Callable) -> Callable:
    @wraps(view)
    def check_login(*args, **kwargs):
        return login_required(view)(*args, **kwargs)

    return check_login


def logout() -> Literal[True]:
    return logout_user()


def get_auth_user() -> AuthUser:
    return current_user


def role_checker(role: Literal["admin", "professor", "student"]):
    def role_checker_wrapper(view: Callable):
        @wraps(view)
        def check_role(*args, **kwargs):
            user = get_auth_user()

            if user.role == role:
                return view(*args, **kwargs)

            flash("Sua conta não tem o nível de permissão necessária", "error")

            match role:
                case "admin":
                    view_back = "admin_views.get_analytics_page"

            return redirect(url_for(view_back))

        return check_role

    return role_checker_wrapper


def init_auth(app: Flask) -> None:
    login_manager.init_app(app)
    login_manager.user_loader(get_user)
    login_manager.login_view = "auth_views.login_view"
    login_manager.login_message = "Por favor, faça seu login antes"
    login_manager.login_message_category = "warn"

    bcrypt.init_app(app)
