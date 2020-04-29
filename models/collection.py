from dataclasses import dataclass
from pathlib import Path
from typing import List, Dict, TypeVar, Generic

from typing_extensions import TypedDict

base_res_path: Path = Path.cwd() / 'data'


def ex_resources_path(tool_id: str, coll_id: int, ex_id: int):
    return base_res_path / tool_id / f'coll_{coll_id}' / f'ex_{ex_id}'


class ExCollKey(TypedDict):
    collectionId: int
    toolId: str


@dataclass()
class ExerciseCollection:
    collectionId: int
    toolId: str
    title: str
    authors: List[str]
    text: str

    def key(self) -> ExCollKey:
        return {
            'collectionId': self.collectionId,
            'toolId': self.toolId
        }


@dataclass()
class ExerciseFile:
    name: str
    fileType: str
    editable: bool
    content: str


@dataclass()
class Topic:
    abbreviation: str
    toolId: str
    title: str


S = TypeVar('S')


@dataclass()
class SampleSolution(Generic[S]):
    id: int
    sample: S


class ExKey(TypedDict):
    exerciseId: int
    collectionId: int
    toolId: str


@dataclass()
class Exercise:
    exerciseId: int
    collectionId: int
    toolId: str
    title: str
    authors: List[str]
    text: str
    topics: List[Topic]
    difficulty: int

    def key(self) -> ExKey:
        return {
            'exerciseId': self.exerciseId,
            'collectionId': self.collectionId,
            'toolId': self.toolId
        }


E = TypeVar('E', bound=Exercise)


@dataclass()
class CollectionAndExes(Generic[E]):
    collection: ExerciseCollection
    exercises: Dict[int, E]


@dataclass()
class Lesson:
    id: int


@dataclass()
class ToolValues:
    collectionAndExes: Dict[int, CollectionAndExes]
    lessons: Dict[int, Lesson]


def load_text_from_file(file_path: Path) -> str:
    return file_path.read_text(encoding='utf-8')
