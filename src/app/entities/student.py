from dataclasses import dataclass

from entities.user import User
from entities.course import Course


@dataclass
class Student(User):
    course: Course = None
