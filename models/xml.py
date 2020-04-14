from dataclasses import dataclass
from enum import Enum

from models.collection import ExerciseContent


class XmlExTag(str, Enum):
    pass


@dataclass()
class XmlSolution:
    document: str
    grammar: str


@dataclass()
class XmlExerciseContent(ExerciseContent[XmlSolution]):
    root_node: str
    grammar_description: str
