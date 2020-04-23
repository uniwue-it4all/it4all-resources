from textwrap import dedent

from models.collection import SampleSolution
from models.sql import SqlExerciseType, SqlExTag, SqlExercise, SqlExerciseContent

sql_coll_1_ex_4: SqlExercise = SqlExercise(
    id=4,
    collectionId=1,
    toolId='sql',
    title='Nutzernamen',
    authors=['bje40dc'],
    text='Geben Sie die Nutzernamen aller Angestellten alphabetisch geordnet aus!',
    topics=[],
    difficulty=1,
    content=SqlExerciseContent(
        exerciseType=SqlExerciseType.SELECT,
        schemaName='employee',
        sampleSolutions=[
            SampleSolution(
                id=1,
                sample=dedent(
                    """\
                    SELECT username
                        FROM employee
                        ORDER BY username;"""
                )
            )
        ],
        tags=[SqlExTag.SQL_ORDER_BY]
    )
)
