from json import load as json_load
from pathlib import Path
from typing import List, Dict, Optional

# noinspection Mypy
from jsonschema import validate as json_schema_validate, RefResolver
from typing_extensions import TypedDict

from models.basics import resource_base_dir, schemas_path

coll_file_name: str = 'collection_metadata.json'

coll_schema_path: Path = schemas_path / 'collection.schema.json'
collection_schema: Dict = json_load(coll_schema_path.open('r'))

coll_resolver: RefResolver = RefResolver(referrer=collection_schema, base_uri=f'file://{schemas_path.absolute()}/')


class ExerciseCollection(TypedDict):
    tool_id: str
    id: int
    title: str
    authors: List[str]
    text: str
    state: str


def get_collection_ids_for_tool(tool_id: str) -> List[int]:
    tool_dir: Path = resource_base_dir / tool_id
    return sorted([int(x.name) for x in tool_dir.glob('*') if x.is_dir()])


def load_collections(tool_id: str) -> List[ExerciseCollection]:
    collections: List[ExerciseCollection] = []

    for collection_id in get_collection_ids_for_tool(tool_id):
        maybe_collection: Optional[ExerciseCollection] = load_collection(tool_id, collection_id)

        if maybe_collection is not None:
            collections.append(maybe_collection)

    return collections


def load_collection(tool_id: str, collection_id: int) -> Optional[ExerciseCollection]:
    metadata_path: Path = resource_base_dir / tool_id / str(collection_id) / coll_file_name

    if not metadata_path.exists():
        return None

    # noinspection PyBroadException
    try:
        maybe_collection: ExerciseCollection = json_load(metadata_path.open('r'))

        json_schema_validate(maybe_collection, schema=collection_schema, resolver=coll_resolver)

        return maybe_collection
    except Exception as e:
        print(e)
        return None
