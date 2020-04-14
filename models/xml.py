from dataclasses import dataclass
from typing import List

from models.collection import SampleSolution


@dataclass()
class XmlSolution:
    document: str
    grammar: str


@dataclass()
class XmlExerciseContent:
    root_node: str
    grammar_description: str
    sample_solutions: List[SampleSolution[XmlSolution]]
