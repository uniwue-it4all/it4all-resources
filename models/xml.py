from dataclasses import dataclass
from typing import List

from models.collection import Exercise, SampleSolution


@dataclass()
class XmlSolution:
    document: str
    grammar: str


@dataclass()
class XmlExerciseContent:
    rootNode: str
    grammarDescription: str
    sampleSolutions: List[SampleSolution[XmlSolution]]


@dataclass()
class XmlExercise(Exercise):
    content: XmlExerciseContent
