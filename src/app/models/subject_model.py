from dataclasses import dataclass
from models.model import Model


@dataclass
class SubjectModel(Model):
    name: str = None
    description: str = None
