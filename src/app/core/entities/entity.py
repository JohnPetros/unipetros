from dataclasses import dataclass
from uuid import uuid4 as generate_id


@dataclass
class Entity:
    id: str = None

    def __post_init__(self):
        self.id = str(generate_id()) if self.id is None else self.id
