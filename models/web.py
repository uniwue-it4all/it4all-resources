from typing import Dict, Any
from models.exercise_file import update_exercise_files_field


def update_web_exercise_content(json: Dict[str, Any]) -> Dict[str, Any]:
    update_exercise_files_field(json, 'files')

    for sample_json in json['sampleSolutions']:
        update_exercise_files_field(sample_json, 'sample')

    return json
