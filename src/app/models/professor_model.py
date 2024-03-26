from dataclasses import dataclass
from typing import List

from models.user_model import UserModel
from models.subject_model import SubjectModel


@dataclass
class ProfessorModel(UserModel):
    subjects: List[SubjectModel] = None
