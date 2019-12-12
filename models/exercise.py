from logging import exception as log_exception
from pathlib import Path
from typing import List, Dict, Any, TypeVar, Union
from json import load as json_load
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


def __update_tags__(exercise: Exercise):
    tag_abbreviations: List[str] = exercise['tags']

    tag_file = resource_base_dir / exercise['toolId'] / 'tags.json'
    tag_mappings: Dict[str, str] = json_load(tag_file.open('r'))

    exercise['tags'] = [
        {
            'abbreviation': tag_ab,
            'title': tag_mappings[tag_ab]
        } for tag_ab in tag_abbreviations
    ]


def update_exercise(exercise: Exercise) -> Exercise:
    __update_tags__(exercise)

    exercise['text'] = read_long_text_from_file(exercise['text'])

    __update_content__(exercise['toolId'], exercise['content'])

    return exercise


def get_exercise_ids_for_collection(tool_id: str, collection_id: int) -> List[int]:
    collection_dir: Path = resource_base_dir / tool_id / str(collection_id)
    return sorted([int(x.name) for x in collection_dir.glob('*') if x.is_dir()])


def load_exercises(tool_id: str, coll_id: int) -> List[Exercise]:
    exercises: List[Exercise] = []

    for ex_id in get_exercise_ids_for_collection(tool_id, coll_id):
        maybe_exercise: Union[str, Exercise] = load_exercise(tool_id, coll_id, ex_id)

        if isinstance(maybe_exercise, Dict):
            exercises.append(maybe_exercise)

    return exercises


def load_exercise(tool_id: str, coll_id: int, ex_id: int, log_errors: bool = True) -> Union[str, Exercise]:
    metadata_file: Path = resource_base_dir / tool_id / str(coll_id) / str(ex_id) / 'exercise_metadata.yaml'

    if not metadata_file.exists():
        return f'Could not find metadata file {metadata_file.absolute()}'

    # noinspection PyBroadException
    try:
        exercise_dict: Dict = yaml_load(metadata_file.open('r'), SafeLoader)
        return update_exercise(exercise_dict)
    except Exception as e:
        if log_errors:
            log_exception(e)
        return str(e)
