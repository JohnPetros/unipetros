from dataclasses import dataclass
from typing import List
from datetime import date

from models.user_model import UserModel
from models.subject_model import SubjectModel


@dataclass
class ProfessorModel(UserModel):
    birthdate: date = None
    age: int = None
    gender: str = None
    subjects: List[SubjectModel] = None
