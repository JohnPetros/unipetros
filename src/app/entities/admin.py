from dataclasses import dataclass

from entities.user import User


@dataclass
class Admin(User):
    created_by: str = "John Petros"
