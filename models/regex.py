from dataclasses import dataclass
from enum import Enum
from typing import List

from models.collection import Exercise, SampleSolution


class RegexCorrectionType(str, Enum):
    MATCHING = "MATCHING"
    EXTRACTION = "EXTRACTION"


@dataclass()
class RegexMatchTestData:
    id: int
    data: str
    isIncluded: bool


@dataclass()
class RegexExtractionTestData:
    id: int
    base: str
    toExtract: List[str]


@dataclass()
class RegexExerciseContent:
    maxPoints: int
    correctionType: RegexCorrectionType
    matchTestData: List[RegexMatchTestData]
    extractionTestData: List[RegexExtractionTestData]
    sampleSolutions: List[SampleSolution[str]]


@dataclass()
class RegexExercise(Exercise):
    content: RegexExerciseContent
