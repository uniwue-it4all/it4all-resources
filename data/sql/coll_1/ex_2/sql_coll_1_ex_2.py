from textwrap import dedent

from models.basics import SampleSolution
from models.sql import SqlExerciseType, SqlExercise, SqlExerciseContent

sql_coll_1_ex_2: SqlExercise = SqlExercise(
    exerciseId=2,
    collectionId=1,
    toolId='sql',
    title='Angestelltennummer',
    authors=['bje40dc'],
    text="""Welche Angestelltennummer (id) hat Max Becker?""",
    difficulty=1,
    content=SqlExerciseContent(
        exerciseType=SqlExerciseType.SELECT,
        schemaName='employee',
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
