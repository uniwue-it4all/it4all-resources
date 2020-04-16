from dataclasses import dataclass

from models.collection import Exercise


@dataclass()
class XmlSolution:
    document: str
    grammar: str


@dataclass()
class XmlExercise(Exercise[XmlSolution]):
    rootNode: str
    grammarDescription: str
