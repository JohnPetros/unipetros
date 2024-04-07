from dataclasses import dataclass

from core.entities.entity import Entity


@dataclass
class Subject(Entity):
    name: str = None
    description: str = None
