from json import load as json_load
from pathlib import Path
from typing import List, Dict, Optional

resource_base_dir = Path.cwd() / 'resources'


def get_tools() -> List[str]:
    return sorted([x.name for x in resource_base_dir.glob('*') if x.is_dir()])


def get_collection_ids_for_tool(tool_id: str) -> List[int]:
    tool_dir: Path = resource_base_dir / tool_id
    return sorted([int(x.name) for x in tool_dir.glob('*') if x.is_dir()])


def get_collection_metadata(tool_id: str, collection_id: int) -> Optional[Dict]:
    metadata_file: Path = resource_base_dir / tool_id / str(collection_id) / 'collection_metadata.json'

    if metadata_file.exists():
        print(metadata_file)

        return json_load(metadata_file.open('r'))

    return None


def get_exercise_ids_for_collection(tool_id: str, collection_id: int) -> List[int]:
    collection_dir: Path = resource_base_dir / tool_id / str(collection_id)
    return sorted([int(x.name) for x in collection_dir.glob('*') if x.is_dir()])
