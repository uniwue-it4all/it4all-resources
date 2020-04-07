from enum import Enum
from json import load as json_load
from logging import exception as log_exception
from pathlib import Path
from typing import List, Optional, Dict, Any, TypedDict

from models.basics import resource_base_dir

ExerciseCollection = Dict[str, Any]


def get_collection_ids_for_tool(tool_id: str) -> List[int]:
    collection_dir: Path = resource_base_dir / tool_id / 'collections'
    return sorted([int(x.name) for x in collection_dir.glob('*') if x.is_dir()])


def load_collections(tool_id: str) -> List[ExerciseCollection]:
    collections: List[ExerciseCollection] = []

    for collection_id in get_collection_ids_for_tool(tool_id):
        maybe_collection: Optional[ExerciseCollection] = load_collection(tool_id, collection_id)

        if maybe_collection is not None:
            collections.append(maybe_collection)

    return collections


def load_collection(tool_id: str, collection_id: int, log_errors: bool = True) -> Optional[ExerciseCollection]:
    metadata_path: Path = resource_base_dir / tool_id / 'collections' / str(collection_id) / 'collection_metadata.json'

    if not metadata_path.exists():
        if log_errors:
            log_exception(f'Could not find metadata file {metadata_path}')
        return None

    # noinspection PyBroadException
    try:
        return json_load(metadata_path.open('r'))
    except Exception as e:
        if log_errors:
            log_exception(e)
        return None


class ToolState(Enum):
    PRE_ALPHA = 'PRE_ALPHA'
    ALPHA = 'ALPHA'
    BETA = 'BETA'
    LIVE = 'LIVE'


class Collection(TypedDict):
    id: int
    tool_id: str
    title: str
    authors: List[str]
    text: str
    short_name: str
