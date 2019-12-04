from json import load as json_load
from pathlib import Path
from typing import Union, List, Any, Optional, Dict, Tuple

# noinspection Mypy
from jsonschema import validate as json_schema_validate, RefResolver
from typing_extensions import TypedDict
from yaml import load as yaml_load, Loader as YamlLoader

from models.basics import LongText, resource_base_dir


class SemanticVersion(TypedDict):
    major: int
    minor: int
    patch: int


class Exercise(TypedDict):
    id: int
    collectionId: int
    toolId: str
    semanticVersion: SemanticVersion
    title: str
    author: List[str]
    text: Union[str, LongText]
    state: str
    content: Any


def __get_ex_schema_file_name__(tool_id: str) -> str:
    return f'{tool_id}_ex_content.schema.json'


def __get_exercise_schema_for_tool__(tool_id: str) -> Tuple[Dict, RefResolver]:
    schema_path: Path = resource_base_dir / tool_id / __get_ex_schema_file_name__(tool_id)

    ex_schema = json_load(schema_path.open('r'))

    ex_resolver: RefResolver = RefResolver(referrer=ex_schema, base_uri=f'file://{schema_path.parent.absolute()}/')

    return ex_schema, ex_resolver


def get_exercise_ids_for_collection(tool_id: str, collection_id: int) -> List[int]:
    collection_dir: Path = resource_base_dir / tool_id / str(collection_id)
    return sorted([int(x.name) for x in collection_dir.glob('*') if x.is_dir()])


def load_exercises(tool_id: str, coll_id: int) -> List[Exercise]:
    exercises: List[Exercise] = []

    for ex_id in get_exercise_ids_for_collection(tool_id, coll_id):
        maybe_exercise = load_exercise(tool_id, coll_id, ex_id)

        if maybe_exercise is not None:
            exercises.append(maybe_exercise)

    return exercises


def load_exercise(tool_id: str, coll_id: int, ex_id: int) -> Optional[Exercise]:
    metadata_file: Path = resource_base_dir / tool_id / str(coll_id) / str(ex_id) / 'exercise_metadata.yaml'

    if not metadata_file.exists():
        return None

    # noinspection PyBroadException
    try:
        loaded: Exercise = yaml_load(metadata_file.open('r'), Loader=YamlLoader)

        exercise_schema, exercise_resolver = __get_exercise_schema_for_tool__(tool_id)
        json_schema_validate(loaded, schema=exercise_schema, resolver=exercise_resolver)

        return loaded
    except Exception as e:
        print(e)
        return None
