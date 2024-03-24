from dataclasses import dataclass
from typing import List
from datetime import date

from models.user_model import UserModel
from helpers.calculate_age import calculate_age


@dataclass
class ProfessorModel(UserModel):
    birthdate: date = None
    age: int = None
    subjects: List[str] = None

    def __post_init__(self) -> None:
        # self.age = calculate_age(self.birthdate)
        self.age = 24
