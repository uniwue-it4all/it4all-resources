from textwrap import dedent

from models.collection import SampleSolution
from models.sql import SqlExerciseType, SqlExercise

sql_coll_1_ex_2: SqlExercise = SqlExercise(
    id=2,
    collectionId=1,
    toolId='sql',
    title='Angestelltennummer',
    authors=['bje40dc'],
    text="""Welche Angestelltennummer (id) hat Max Becker?""",
    topics=[],
    difficulty=1,
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
