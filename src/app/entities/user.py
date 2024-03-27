from dataclasses import dataclass
from datetime import date

from entities.entity import Entity

from helpers.calculate_age import calculate_age


@dataclass
class User(Entity):
    name: str = None
    email: str = None
    password: str = None
    avatar: str = None
    phone: str = None
    gender: str = None
    age: int = None
    birthdate: date = None

    def __post_init__(self) -> None:
        super().__post_init__()

        if self.birthdate is not None:
            self.age = calculate_age(self.birthdate)
