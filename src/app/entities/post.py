from typing import Literal

from dataclasses import dataclass

from entities.entity import Entity
from entities.user import User


@dataclass
class Post(Entity):
    title: str = None
    content: str = None
    category: Literal["academic", "sport", "study_tip"] = "academic"
    author: User = None
