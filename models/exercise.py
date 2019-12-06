from logging import exception as log_exception
from pathlib import Path
from typing import List, Optional, Dict, Any, TypeVar

from yaml import load as yaml_load, SafeLoader

from models.basics import resource_base_dir, read_long_text_from_file
from models.programming import update_programming_exercise_content
from models.web import update_web_exercise_content

EC = TypeVar('EC')

Exercise = Dict[str, Any]


def __update_content__(tool_id: str, json: Dict[str, Any]) -> Dict[str, Any]:
    if tool_id == 'programming':
        return update_programming_exercise_content(json)
    elif tool_id == 'regex':
        return json
    elif tool_id == 'web':
        return update_web_exercise_content(json)
    else:
        return json


def update_exercise(exercise: Exercise) -> 'Exercise':
    exercise['text'] = read_long_text_from_file(exercise['text'])

    __update_content__(exercise['toolId'], exercise['content'])

    return exercise


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


def load_exercise(tool_id: str, coll_id: int, ex_id: int, log_errors: bool = True) -> Optional[Exercise]:
    metadata_file: Path = resource_base_dir / tool_id / str(coll_id) / str(ex_id) / 'exercise_metadata.yaml'

    if not metadata_file.exists():
        if log_errors:
            print(f'Could not find metadata file {metadata_file.absolute()}')
        return None

    # noinspection PyBroadException
    try:
        exercise_dict: Dict = yaml_load(metadata_file.open('r'), SafeLoader)
        return update_exercise(exercise_dict)
    except Exception as e:
        if log_errors:
            log_exception(e)
        return None
