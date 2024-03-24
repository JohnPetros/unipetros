from dataclasses import dataclass

from models.model import Model


@dataclass
class UserModel(Model):
    name: str = None
    email: str = None
    password: str = None
    avatar: str = None
