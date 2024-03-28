from typing import Literal
from dataclasses import asdict

from repositories import StudentsRepository, ProfessorsRepository, AdminsRepository

from utils.error import Error

from auth import AuthUser, check_password, login


class LoginUseCase:
    def execute(
        self,
        email: str,
        password: str,
        role: Literal["admin", "professor", "student"],
        should_remember_user: bool,
    ) -> AuthUser | None:
        match role:
            case "admin":
                admins_repository = AdminsRepository(should_get_password=True)
                user = admins_repository.get_admin_by_email(email)
            case "professor":
                professors_repository = ProfessorsRepository(should_get_password=True)
                user = professors_repository.get_professor_by_email(email)
            case "student":
                students_repository = StudentsRepository(should_get_password=True)
                user = students_repository.get_student_by_email(email)
            case _:
                raise Error(f"Invalid role: {role}")

        if not user or not check_password(user.password, password):
            return None

        auth_user = AuthUser(role=role, **asdict(user))

        is_login_success = login(auth_user, should_remember_user=should_remember_user)

        return auth_user if is_login_success else None
