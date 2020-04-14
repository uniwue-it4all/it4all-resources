from dataclasses import dataclass
from enum import Enum
from typing import List, Any

from models.collection import ExerciseFile, SampleSolution


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
class ProgrammingExerciseContent:
    functionName: str
    foldername: str
    filename: str
    inputTypes: List[ProgrammingInput]
    outputType: str
    unitTestPart: ProgrammingUnitTestPart
    implementationPart: ProgrammingImplementationPart
    sampleSolutions: List[SampleSolution[ProgrammingSolution]]
    sampleTestData: List[ProgrammingTestData]
