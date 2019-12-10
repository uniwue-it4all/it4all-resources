from pathlib import Path
from typing import Dict, Any, List

resource_base_dir: Path = Path.cwd() / 'resources'
schemas_path: Path = Path.cwd() / 'schemas'


def get_all_tool_ids() -> List[str]:
    return sorted([x.name for x in resource_base_dir.glob('*') if x.is_dir()])


def get_tool_dir(tool_id: str) -> Path:
    return resource_base_dir / tool_id


# LongText

def read_long_text_from_file(json: Dict[str, Any]) -> str:
    file_path: Path = resource_base_dir / json['relativePath']
    return file_path.read_text()


# ExerciseFile

def update_exercise_file(json_file: Dict[str, Any]):
    resource_path: Path = resource_base_dir / json_file['resourcePath']

    json_file['content'] = resource_path.read_text()


def update_exercise_files_field(json: Dict[str, Any], field_name: str):
    for json_file in json[field_name]:
        update_exercise_file(json_file)
