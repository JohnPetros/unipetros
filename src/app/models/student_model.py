from typing import List
from models.user_model import UserModel


class StudentModel(UserModel):
    courses: List[str] = None
