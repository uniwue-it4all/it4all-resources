from dataclasses import dataclass, field
from enum import Enum
from typing import List

from models.collection import SampleSolution


class UmlClassType(str, Enum):
    CLASS = 'CLASS'
    ABSTRACT = 'ABSTRACT'
    INTERFACE = 'INTERFACE'


class UmlVisibility(str, Enum):
    PUBLIC = 'PUBLIC'


@dataclass()
class UmlAttribute:
    memberName: str
    memberType: str
    visibility: UmlVisibility = field(default=UmlVisibility.PUBLIC)
    isAbstract: bool = field(default=False)
    isDerived: bool = field(default=False)
    isStatic: bool = field(default=False)


@dataclass()
class UmlMethod:
    memberName: str
    parameters: str
    memberType: str
    isAbstract: bool = field(default=False)
    isStatic: bool = field(default=False)


@dataclass()
class UmlClass:
    name: str
    classType: UmlClassType = field(default=UmlClassType.CLASS)
    attributes: List[UmlAttribute] = field(default_factory=list)
    methods: List[UmlMethod] = field(default_factory=list)


class UmlAssociationType(str, Enum):
    ASSOCIATION = 'ASSOCIATION'
    AGGREGATION = 'AGGREGATION'
    COMPOSITION = 'COMPOSITION'


class UmlMultiplicity(str, Enum):
    SINGLE = 'SINGLE'
    UNBOUND = 'UNBOUND'


@dataclass()
class UmlAssociation:
    firstEnd: str
    firstMult: UmlMultiplicity
    secondEnd: str
    secondMult: UmlMultiplicity
    assocType: UmlAssociationType = field(default=UmlAssociationType.ASSOCIATION)


@dataclass()
class UmlImplementation:
    subClass: str
    superClass: str


@dataclass()
class UmlClassDiagram:
    classes: List[UmlClass]
    associations: List[UmlAssociation]
    implementations: List[UmlImplementation]


@dataclass()
class UmlMapping:
    key: str
    value: str


@dataclass()
class UmlExerciseContent:
    toIgnore: List[str]
    mappings: List[UmlMapping]
    sampleSolutions: List[SampleSolution[UmlClassDiagram]]
