from textwrap import dedent

from models.collection import ExerciseState, Exercise, SampleSolution, SemanticVersion
from models.sql import SqlExerciseContent, SqlExerciseType

sql_coll_1_ex_2 = Exercise(
    id=2,
    collectionId=1,
    toolId='sql',
    semanticVersion=SemanticVersion(major=1, minor=0, patch=0),
    title='Angestelltennummer',
    authors=['bje40dc'],
    text="""Welche Angestelltennummer (id) hat Max Becker?""",
    tags=[],
    state=ExerciseState.APPROVED,
    difficulty=1,
    content=SqlExerciseContent(
        exerciseType=SqlExerciseType.SELECT,
        sampleSolutions=[
            SampleSolution(
                id=1,
                sample=dedent(
                    """\
                    SELECT id
                        FROM employee
                        WHERE firstname = 'Max' AND lastname = 'Becker';"""
                )
            )
        ]
    )
)
