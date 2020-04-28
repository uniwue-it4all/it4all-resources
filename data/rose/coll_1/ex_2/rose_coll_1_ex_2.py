from pathlib import Path

from models.collection import load_text_from_file, ex_resources_path, SampleSolution
from models.rose import RoseExercise, RoseExerciseContent

ex_res_path: Path = ex_resources_path('rose', 1, 2)

rose_coll_1_ex_2 = RoseExercise(
    exerciseId=2,
    collectionId=1,
    toolId='rose',
    title='Kaninchenjagd',
    authors=['bje40dc'],
    text=load_text_from_file(ex_res_path / 'text.html'),
    topics=[],
    difficulty=1,
    content=RoseExerciseContent(
        fieldWidth=8,
        fieldHeight=10,
        isMultiplayer=False,

        inputTypes=[
            {'id': 1, 'name': 'rabbit_x', 'type': 'int'},
            {'id': 2, 'name': 'rabbit_y', 'type': 'int'}
        ],

        sampleSolutions=[
            SampleSolution(
                id=1,
                sample=load_text_from_file(ex_res_path / 'sol_1' / 'robot.py')
            )
        ]
    )
)
