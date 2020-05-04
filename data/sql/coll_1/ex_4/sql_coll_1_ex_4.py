from textwrap import dedent

from models.basics import SampleSolution
from models.sql import SqlExerciseType, SqlExTag, SqlExercise, SqlExerciseContent

sql_coll_1_ex_4: SqlExercise = SqlExercise(
    exerciseId=4,
    collectionId=1,
    toolId='sql',
    title='Nutzernamen',
    authors=['bje40dc'],
    text='Geben Sie die Nutzernamen aller Angestellten alphabetisch geordnet aus!',
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
