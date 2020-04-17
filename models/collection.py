from dataclasses import dataclass
from pathlib import Path
from typing import List, Dict, TypeVar, Generic, Any

base_res_path: Path = Path.cwd() / 'data'


def ex_resources_path(tool_id: str, coll_id: int, ex_id: int):
    return base_res_path / tool_id / f'coll_{coll_id}' / f'ex_{ex_id}'


@dataclass()
class Collection:
    id: int
    toolId: str
    title: str
    authors: List[str]
    text: str
    shortName: str


@dataclass()
class ExerciseFile:
    name: str
    fileType: str
    editable: bool
    content: str


@dataclass()
class Topic:
    x: Any


S = TypeVar('S')


@dataclass()
class SampleSolution(Generic[S]):
    id: int
    sample: S


EC = TypeVar('EC')


@dataclass()
class Exercise(Generic[S, EC]):
    id: int
    collectionId: int
    toolId: str
    title: str
    authors: List[str]
    text: str
    topics: List[Topic]
    difficulty: int
    sampleSolutions: List[SampleSolution[S]]
    content: EC


E = TypeVar('E', bound=Exercise)


@dataclass()
class CollectionAndExes(Generic[E]):
    collection: Collection
    exercises: Dict[int, E]


@dataclass()
class Lesson:
    id: int


@dataclass()
class ToolValues:
    collections: Dict[int, CollectionAndExes]
    lessons: Dict[int, Lesson]


def load_text_from_file(file_path: Path) -> str:
    return file_path.read_text()
