from typing import Dict, Any

from models.basics import update_exercise_files_field


def update_programming_exercise_content(json: Dict[str, Any]) -> Dict[str, Any]:
    update_exercise_files_field(json['unitTestPart'], 'unitTestFiles')

    update_exercise_files_field(json['implementationPart'], 'files')

    for sample_json in json['sampleSolutions']:
        update_exercise_files_field(sample_json['sample'], 'files')

    return json
