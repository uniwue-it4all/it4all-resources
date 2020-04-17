from dataclasses import dataclass

from models.collection import Exercise


@dataclass()
class XmlSolution:
    document: str
    grammar: str


@dataclass()
class XmlExerciseContent:
    rootNode: str
    grammarDescription: str


@dataclass()
class XmlExercise(Exercise[XmlSolution, XmlExerciseContent]):
    pass
