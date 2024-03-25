from dataclasses import dataclass

from models.model import Model

from helpers.calculate_age import calculate_age


@dataclass
class UserModel(Model):
    name: str = None
    email: str = None
    password: str = None
    avatar: str = None
    phone: str = None
    gender: str = None

    def __post_init__(self) -> None:
        super().__post_init__()

        if self.birthdate is not None:
            self.age = calculate_age(self.birthdate)
