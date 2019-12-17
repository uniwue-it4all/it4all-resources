from pathlib import Path
from typing import Dict, Any, List

resource_base_dir: Path = Path.cwd() / 'resources'
schemas_path: Path = Path.cwd() / 'schemas'


def get_all_tool_ids() -> List[str]:
    return sorted([x.name for x in resource_base_dir.glob('*') if x.is_dir()])


# LongText

def read_long_text_from_file(exercise_base_path: Path, json: Dict[str, Any]) -> str:
    file_path: Path = exercise_base_path / json['relativePath']

    return file_path.read_text()


# ExerciseFile

def update_exercise_file(base_path: Path, json_file: Dict[str, Any]):
    resource_path: Path = base_path / json_file['resourcePath']
    json_file['content'] = resource_path.read_text()


def update_exercise_files_field(base_path: Path, files_field: Dict[str, Any], field_name: str):
    for json_file in files_field[field_name]:
        update_exercise_file(base_path, json_file)
