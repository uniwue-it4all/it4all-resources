from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import List, Dict, TypeVar, Generic

base_res_path: Path = Path.cwd() / 'data'

S = TypeVar('S')
T = TypeVar('T')


@dataclass()
class SampleSolution(Generic[S]):
    id: int
    sample: S


@dataclass()
class ExerciseContent(Generic[S]):
    sampleSolutions: List[SampleSolution[S]]


CT = TypeVar('CT', bound=ExerciseContent)


class ExerciseState(str, Enum):
    APPROVED = 'APPROVED'
    CREATED = 'CREATED'


@dataclass()
class ExerciseFile:
    name: str
    fileType: str
    editable: bool
    content: str


@dataclass()
class SemanticVersion:
    major: int
    minor: int
    patch: int


@dataclass()
class Exercise(Generic[T, CT]):
    id: int
    collectionId: int
    toolId: str
    semanticVersion: SemanticVersion
    title: str
    authors: List[str]
    text: str
    tags: List[T]
    state: ExerciseState
    difficulty: int
    content: CT


@dataclass()
class Collection:
    id: int
    toolId: str
    title: str
    authors: List[str]
    text: str
    shortName: str


@dataclass()
class CollectionAndExes(Generic[T, CT]):
    collection: Collection
    exercises: Dict[int, Exercise[T, CT]]


@dataclass()
class Lesson:
    id: int


@dataclass()
class ToolValues:
    collections: Dict[int, CollectionAndExes]
    lessons: Dict[int, Lesson]


def load_text_from_file(file_path: Path) -> str:
    return file_path.read_text()
