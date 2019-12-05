from dataclasses import dataclass
from logging import exception as log_exception
from pathlib import Path
from typing import List, Optional, Dict, Any

# noinspection Mypy
from typed_json_dataclass import TypedJsonMixin, MappingMode

from models.basics import get_tool_dir


@dataclass
class ExerciseCollection(TypedJsonMixin):
    tool_id: str
    id: int
    title: str
    authors: List[str]
    text: str
    state: str
    short_name: str

    def to_json_dict(self) -> Dict[str, Any]:
        return {
            'toolId': self.tool_id,
            'id': self.id,
            'title': self.title,
            'authors': self.authors,
            'text': self.text,
            'state': self.state,
            'shortName': self.short_name
        }


def get_collection_ids_for_tool(tool_id: str) -> List[int]:
    return sorted([int(x.name) for x in get_tool_dir(tool_id).glob('*') if x.is_dir()])


def load_collections(tool_id: str) -> List[ExerciseCollection]:
    collections: List[ExerciseCollection] = []

    for collection_id in get_collection_ids_for_tool(tool_id):
        maybe_collection: Optional[ExerciseCollection] = load_collection(tool_id, collection_id)

        if maybe_collection is not None:
            collections.append(maybe_collection)

    return collections


def load_collection(tool_id: str, collection_id: int, log_erros: bool = True) -> Optional[ExerciseCollection]:
    metadata_path: Path = get_tool_dir(tool_id) / str(collection_id) / 'collection_metadata.json'

    if not metadata_path.exists():
        if log_erros:
            log_exception(f'Could not find metadata file {metadata_path}')
        return None

    # noinspection PyBroadException
    try:
        return ExerciseCollection.from_json(metadata_path.read_text(), mapping_mode=MappingMode.SnakeCase)
    except Exception as e:
        if log_erros:
            log_exception(e)
        return None
