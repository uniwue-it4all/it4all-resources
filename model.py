from json import load as json_load
from pathlib import Path
from typing import List, Dict, Optional

import yaml

from models.exercise import Exercise, resource_base_dir


def get_tool_ids() -> List[str]:
    return sorted([x.name for x in resource_base_dir.glob('*') if x.is_dir()])


def tool_exists(tool_id: str) -> bool:
    tool_path: Path = resource_base_dir / tool_id
    return tool_path.exists() and tool_path.is_dir()


def get_collection_ids_for_tool(tool_id: str) -> List[int]:
    tool_dir: Path = resource_base_dir / tool_id
    return sorted([int(x.name) for x in tool_dir.glob('*') if x.is_dir()])


def collection_exists(tool_id: str, coll_id: int) -> bool:
    metadata_file: Path = resource_base_dir / tool_id / str(coll_id) / 'collection_metadata.json'
    return metadata_file.exists()


def get_collection_metadata(tool_id: str, coll_id: int) -> Optional[Dict]:
    metadata_file: Path = resource_base_dir / tool_id / str(coll_id) / 'collection_metadata.json'

    if metadata_file.exists():
        return json_load(metadata_file.open('r'))

    return None


def get_exercise_ids_for_collection(tool_id: str, collection_id: int) -> List[int]:
    collection_dir: Path = resource_base_dir / tool_id / str(collection_id)
    return sorted([int(x.name) for x in collection_dir.glob('*') if x.is_dir()])


def get_exercise_metadata(tool_id: str, coll_id: int, ex_id: int) -> Optional[Exercise]:
    metadata_file: Path = resource_base_dir / tool_id / str(coll_id) / str(ex_id) / 'exercise_metadata.yaml'

    if not metadata_file.exists():
        return None

    return yaml.load(metadata_file.open('r'), Loader=yaml.Loader)
