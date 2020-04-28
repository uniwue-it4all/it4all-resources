from pathlib import Path

from models.collection import load_text_from_file, ex_resources_path, SampleSolution
from models.rose import RoseExerciseContent, RoseExercise

ex_res_path: Path = ex_resources_path('rose', 1, 1)

rose_coll_1_ex_1 = RoseExercise(
    exerciseId=1,
    collectionId=1,
    toolId='rose',
    title='Zeichnen eines Rechtecks',
    authors=['bje40dc'],
    topics=[],
    text=load_text_from_file(ex_res_path / 'text.html'),
    difficulty=1,
    content=RoseExerciseContent(
        fieldWidth=8,
        fieldHeight=10,
        isMultiplayer=False,
        inputTypes=[
            {'id': 1, 'name': 'width', 'type': 'int'},
            {'id': 2, 'name': 'height', 'type': 'int'}
        ],
        sampleSolutions=[
            SampleSolution(
                id=1,
                sample=load_text_from_file(ex_res_path / 'sol_1' / 'robot.py')
            )
        ]
    )
)
