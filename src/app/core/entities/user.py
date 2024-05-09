from dataclasses import dataclass
from datetime import date

from core.entities.entity import Entity
from core.commons.age import Age


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
            age = Age(self.birthdate)
            self.age = age.get_value()
