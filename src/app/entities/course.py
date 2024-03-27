from dataclasses import dataclass

from entities.entity import Entity


@dataclass
class Course(Entity):
    name: str = None
    description: str = None
