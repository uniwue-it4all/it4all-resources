from dataclasses import dataclass
from logging import exception as log_exception
from pathlib import Path
from typing import List, Optional, Dict, Any, TypeVar, Generic

from yaml import load as yaml_load, SafeLoader

from models.basics import LongText, resource_base_dir
from models.programming import update_programming_exercise_content
from models.web import update_web_exercise_content

EC = TypeVar('EC')


@dataclass()
class Exercise(Generic[EC]):
    id: int
    collection_id: int
    tool_id: str
    semantic_version: Dict
    title: str
    authors: List[str]
    text: LongText
    state: str
    tags: List[str]
    content: EC

    @staticmethod
    def __update_content__(tool_id: str, json: Dict[str, Any]) -> Dict[str, Any]:
        if tool_id == 'programming':
            return update_programming_exercise_content(json)
        elif tool_id == 'regex':
            return json
        elif tool_id == 'web':
            return update_web_exercise_content(json)
        else:
            return json

    @staticmethod
    def from_json(json: Dict[str, Any]) -> 'Exercise':
        tool_id: str = str(json['toolId'])

        return Exercise(
            int(json['id']),
            int(json['collectionId']),
            tool_id,
            json['semanticVersion'],
            str(json['title']),
            list(map(lambda a: str(a), json['authors'])),
            LongText.from_json(json['text']),
            str(json['state']),
            list(map(lambda t: str(t), json['tags'])),
            Exercise.__update_content__(tool_id, json['content'])
        )

    def to_json(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'collectionId': self.collection_id,
            'toolId': self.tool_id,
            'semanticVersion': self.semantic_version,
            'title': self.title,
            'authors': self.authors,
            'text': self.text.to_json_dict(),
            'state': self.state,
            'tags': self.tags,
            'content': self.content
        }


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
        return Exercise.from_json(exercise_dict)
    except Exception as e:
        if log_errors:
            log_exception(e)
        return None
