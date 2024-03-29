from dataclasses import dataclass
from datetime import date

from entities.user import User
from entities.course import Course


@dataclass
class Student(User):
    course: Course = None
    created_at: date = None
