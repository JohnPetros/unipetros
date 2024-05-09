from dataclasses import dataclass
from typing import List

from core.entities.user import User
from core.entities.subject import Subject


@dataclass
class Professor(User):
    subjects: List[Subject] = None
