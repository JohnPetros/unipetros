from dataclasses import dataclass
from datetime import date

from entities.user import User
from entities.course import Course


@dataclass
class Student(User):
    course: Course = None
    is_active: bool = True
    created_at: date = None
