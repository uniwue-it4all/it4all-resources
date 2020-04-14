from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import List, Dict, TypeVar, Generic, Any

T = TypeVar('T')

base_res_path: Path = Path.cwd() / 'data'


class ExerciseState(str, Enum):
    APPROVED = 'APPROVED'
    CREATED = 'CREATED'


@dataclass()
class ExerciseFile:
    name: str
    file_type: str
    editable: bool
    content: str


@dataclass()
class SemanticVersion:
    major: int
    minor: int
    patch: int


@dataclass()
class SampleSolution(Generic[T]):
    id: int
    sample: T


@dataclass()
class Exercise(Generic[T]):
    id: int
    collectionId: int
    toolId: str
    semanticVersion: SemanticVersion
    title: str
    authors: List[str]
    text: str
    tags: List[Any]
    state: ExerciseState
    difficulty: int
    content: T


@dataclass()
class Collection:
    id: int
    toolId: str
    title: str
    authors: List[str]
    text: str
    shortName: str


@dataclass()
class CollectionAndExes(Generic[T]):
    collection: Collection
    exercises: Dict[int, Exercise[T]]


@dataclass()
class Lesson:
    id: int


@dataclass()
class ToolValues:
    collections: Dict[int, CollectionAndExes]
    lessons: Dict[int, Lesson]


def load_text_from_file(file_path: Path) -> str:
    return file_path.read_text()
