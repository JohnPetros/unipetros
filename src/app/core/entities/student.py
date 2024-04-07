from dataclasses import dataclass
from datetime import date

from core.entities.user import User
from core.entities.course import Course


@dataclass
class Student(User):
    course: Course = None
    is_active: bool = True
    created_at: date = None
