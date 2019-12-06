from typing import Dict, Any, List

from models.exercise_file import update_exercise_files_field


def __update_unit_test_part__(json: Dict[str, Any]):
    update_exercise_files_field(json, 'unitTestFiles')


def __update_implementation_part__(json: Dict[str, Any]):
    update_exercise_files_field(json, 'files')


def __update_sample_solutions__(jsons: List[Dict[str, Any]]):
    for json in jsons:
        update_exercise_files_field(json['sample'], 'files')


def update_programming_exercise_content(json: Dict[str, Any]) -> Dict[str, Any]:
    __update_unit_test_part__(json['unitTestPart'])

    __update_implementation_part__(json['implementationPart'])

    __update_sample_solutions__(json['sampleSolutions'])

    return json
