from dataclasses import dataclass
from enum import Enum
from typing import List, Any, Optional

from models.collection import ExerciseFile, Exercise, SampleSolution, Topic


class ProgrammingExTag:
    ForLoops = Topic('FL', 'programming', 'For-Schleifen')
    Conditions = Topic('C', 'programming', 'Bedingungen')
    Maths = Topic('M', 'programming', 'Mathematik')
    Strings = Topic('S', 'programming', 'Strings')
    Lists = Topic('L', 'programming', 'Listen')
    Tuples = Topic('T', 'programming', 'Tuple')
    Classes = Topic('CL', 'programming', 'Klassen')
    Exceptions = Topic('E', 'programming', 'Exceptions')
    Recursions = Topic('R', 'programming', 'Rekursion')
    Dicts = Topic('D', 'programming', 'Dictionaries')


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
    id: int
    shouldFail: bool
    description: str
    file: ExerciseFile


@dataclass()
class ProgrammingUnitTestPart:
    unitTestType: ProgrammingUnitTestType
    unitTestsDescription: str
    unitTestFiles: List[ExerciseFile]
    unitTestTestConfigs: List[ProgrammingUnitTestTestConfig]
    testFileName: str
    sampleSolFileNames: List[str]
    simplifiedTestMainFile: Optional[ExerciseFile] = None


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
class ProgrammingExerciseContent:
    functionName: str
    foldername: str
    filename: str
    inputTypes: List[ProgrammingInput]
    outputType: str
    unitTestPart: ProgrammingUnitTestPart
    implementationPart: ProgrammingImplementationPart
    sampleTestData: List[ProgrammingTestData]
    sampleSolutions: List[SampleSolution[ProgrammingSolution]]


@dataclass()
class ProgrammingExercise(Exercise):
    content: ProgrammingExerciseContent
