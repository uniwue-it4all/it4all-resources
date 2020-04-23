from textwrap import dedent

from models.collection import SampleSolution
from models.sql import SqlExerciseType, SqlExercise, SqlExerciseContent

sql_coll_1_ex_8: SqlExercise = SqlExercise(
    id=8,
    collectionId=1,
    toolId='sql',
    title='Kündigung',
    authors=['bje40dc'],
    text="""Der Angestellte mit der OID 7 hat gekündigt. Löschen Sie ihn aus der Angestelltentabelle.""",
    topics=[],
    difficulty=1,
    content=SqlExerciseContent(
        exerciseType=SqlExerciseType.DELETE,
        schemaName='employee',
        sampleSolutions=[
            SampleSolution(
                id=1,
                sample=dedent(
                    """\
                    DELETE FROM employee
                        WHERE id = 7;"""
                )
            )
        ]
    )
)
