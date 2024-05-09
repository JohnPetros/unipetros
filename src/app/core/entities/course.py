from typing import List

from dataclasses import dataclass

from core.entities.entity import Entity
from core.entities.subject import Subject


@dataclass
class Course(Entity):
    name: str = None
    description: str = None
    subjects: List[Subject] = None
