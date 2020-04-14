from dataclasses import dataclass
from enum import Enum
from typing import List

from models.collection import ExerciseContent


class RegexCorrectionType(str, Enum):
    MATCHING = "MATCHING"
    EXTRACTION = "EXTRACTION"


class RegexExTag(str, Enum):
    pass


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
class RegexExerciseContent(ExerciseContent[str]):
    maxPoints: int
    correctionType: RegexCorrectionType
    matchTestData: List[RegexMatchTestData]
    extractionTestData: List[RegexExtractionTestData]
