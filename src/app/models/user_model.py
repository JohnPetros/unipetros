from typing import Dict
from uuid import uuid4 as generate_id


class UserModel:
    def __init__(self, user: Dict, id: str = None) -> None:
        self.id = str(generate_id()) if id is None else id
        self.name = user["name"]
        self.email = user["email"]
        self.password = user["password"]
        self.avatar = user["avatar"]
        self.role = user["role"]
