from typing import Literal
from dataclasses import dataclass

from models.admin_model import AdminModel
from models.professor_model import ProfessorModel
from models.student_model import StudentModel


@dataclass
class AuthUser(AdminModel, ProfessorModel, StudentModel):
    role: Literal["admin", "professor", "student"] = "admin"
    is_active: bool = True

    def get_id(self) -> str:
        return {"id": self.id, "role": self.role}

    def is_authenticated(self):
        return self.is_active
