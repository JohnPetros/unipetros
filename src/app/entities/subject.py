from dataclasses import dataclass
from entities.entity import Entity


@dataclass
class Subject(Entity):
    name: str = None
    description: str = None
