from pathlib import Path
from typing import Dict, Any

from models.basics import resource_base_dir


def update_exercise_files_field(json: Dict[str, Any], field_name: str):
    for json_file in json[field_name]:
        __update_exercise_content__(json_file)


def __update_exercise_content__(json: Dict[str, Any]):
    resource_path: Path = resource_base_dir / json['resourcePath']

    json['content'] = resource_path.read_text()
