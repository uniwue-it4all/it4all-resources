from pathlib import Path
from typing import Dict, Any

from models.basics import update_exercise_files_field, update_exercise_file


def update_programming_exercise_content(exercise_base_dir: Path, content: Dict[str, Any]) -> Dict[str, Any]:
    # Update UnitTestPart
    unit_test_part: Dict[str, Any] = content['unitTestPart']

    update_exercise_files_field(exercise_base_dir, unit_test_part, 'unitTestFiles')

    for unit_test_config in unit_test_part['unitTestTestConfigs']:
        update_exercise_file(exercise_base_dir, unit_test_config['file'])

    if 'simplifiedTestMainFile' in unit_test_part:
        update_exercise_file(exercise_base_dir, unit_test_part['simplifiedTestMainFile'])

    # Update ImplementationPart
    update_exercise_files_field(exercise_base_dir, content['implementationPart'], 'files')

    # Update SampleSolution
    for sample_json in content['sampleSolutions']:
        update_exercise_files_field(exercise_base_dir, sample_json['sample'], 'files')

    return content
