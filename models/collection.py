from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import List, Dict, TypeVar, Generic, Any

T = TypeVar('T')

base_res_path = Path.cwd() / 'data'


class ExerciseState(str, Enum):
    APPROVED = 'APPROVED'


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
    collection_id: int
    tool_id: str
    semantic_version: SemanticVersion
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
    tool_id: str
    title: str
    authors: List[str]
    text: str
    short_name: str


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
