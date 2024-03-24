from typing import Literal, Union
from dataclasses import asdict

from repositories.admins_repository import AdminsRepository
from repositories.professors_repository import ProfessorsRepository
from repositories.students_repository import StudentsRepository

from auth import AuthUser, check_password, login


class AuthController:
    def handle_login(
        self,
        email: str,
        password: str,
        role: Literal["admin", "professor", "student"],
        should_remember_user: bool,
    ) -> Union[AuthUser, None]:
        match role:
            case "admin":
                admins_repository = AdminsRepository()
                user = admins_repository.get_admin_by_email(email)
            case "professor":
                professors_repository = ProfessorsRepository(True)
                user = professors_repository.get_professor_by_email(email)
            case "student":
                students_repository = StudentsRepository()
                user = students_repository.get_student_by_email(email)

        if not user or not check_password(user.password, password):
            return None

        auth_user = AuthUser(role=role, **asdict(user))

        is_login_success = login(auth_user, should_remember_user=should_remember_user)

        return auth_user if is_login_success else None
