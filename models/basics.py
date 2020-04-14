from pathlib import Path
from typing import Dict, Any

resource_base_dir: Path = Path.cwd() / 'resources'


# ExerciseFile

def update_exercise_file(base_path: Path, json_file: Dict[str, Any]):
    resource_path: Path = base_path / json_file['resourcePath']
    json_file['content'] = resource_path.read_text()


def update_exercise_files_field(base_path: Path, files_field: Dict[str, Any], field_name: str):
    for json_file in files_field[field_name]:
        update_exercise_file(base_path, json_file)
