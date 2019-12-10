from typing import Dict, Any

from models.basics import update_exercise_files_field, update_exercise_file


def update_programming_exercise_content(json: Dict[str, Any]) -> Dict[str, Any]:
    # Update UnitTestPart
    unit_test_part: Dict[str, Any] = json['unitTestPart']

    update_exercise_files_field(unit_test_part, 'unitTestFiles')

    for unit_test_config in unit_test_part['unitTestTestConfigs']:
        update_exercise_file(unit_test_config['file'])

    if 'simplifiedTestMainFile' in unit_test_part:
        update_exercise_file(unit_test_part['simplifiedTestMainFile'])

    # Update ImplementationPart
    update_exercise_files_field(json['implementationPart'], 'files')

    # Update SampleSolution
    for sample_json in json['sampleSolutions']:
        update_exercise_files_field(sample_json['sample'], 'files')

    return json
