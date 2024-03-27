from dataclasses import dataclass
from typing import List

from entities.user import User
from entities.subject import Subject


@dataclass
class Professor(User):
    subjects: List[Subject] = None
