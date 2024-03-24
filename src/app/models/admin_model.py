from dataclasses import dataclass

from models.user_model import UserModel


@dataclass
class AdminModel(UserModel):
    created_by: str = "John Petros"
