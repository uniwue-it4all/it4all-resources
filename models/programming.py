from dataclasses import dataclass
from enum import Enum
from typing import List, Any

from models.collection import ExerciseFile, ExerciseContent


class ProgrammingExTag(str, Enum):
    ForLoops = 'For-Schleifen'
    Conditions = 'Bedingungen'
    Maths = 'Mathematik'
    Strings = 'Strings'
    Lists = 'Listen'
    Tuples = 'Tuple'
    Classes = 'Klassen'
    Exceptions = 'Exceptions'
    Recursions = 'Rekursion'
    Dicts = 'Dictionaries'


class ProgrammingUnitTestType(str, Enum):
    Simplified = 'Simplified'
    Normal = 'Normal'


@dataclass()
class ProgrammingInput:
    id: int
    inputName: str
    inputType: str


@dataclass()
class ProgrammingUnitTestTestConfig:
    pass


@dataclass()
class ProgrammingUnitTestPart:
    unitTestType: ProgrammingUnitTestType
    unitTestsDescription: str
    unitTestFiles: List[ExerciseFile]
    unitTestTestConfigs: List[ProgrammingUnitTestTestConfig]
    simplifiedTestMainFile: ExerciseFile
    testFileName: str
    sampleSolFileNames: List[str]


@dataclass()
class ProgrammingImplementationPart:
    base: str
    files: List[ExerciseFile]
    implFileName: str
    sampleSolFileNames: List[str]


@dataclass()
class ProgrammingSolution:
    files: List[ExerciseFile]
    testData: List[Any]


@dataclass()
class ProgrammingTestData:
    id: int
    input: Any
    output: Any


@dataclass()
class ProgrammingExerciseContent(ExerciseContent[ProgrammingSolution]):
    functionName: str
    foldername: str
    filename: str
    inputTypes: List[ProgrammingInput]
    outputType: str
    unitTestPart: ProgrammingUnitTestPart
    implementationPart: ProgrammingImplementationPart
    sampleTestData: List[ProgrammingTestData]
