from typing import Literal
from dataclasses import dataclass

from core.entities.admin import Admin
from core.entities.professor import Professor
from core.entities.student import Student


@dataclass
class AuthUser(Admin, Professor, Student):
    role: Literal["admin", "professor", "student"] = "admin"
    is_active: bool = True

    def get_id(self) -> str:
        return {"id": self.id, "role": self.role}

    @property
    def is_authenticated(self):
        return self.is_active
