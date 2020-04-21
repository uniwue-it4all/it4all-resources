from textwrap import dedent

from models.collection import SampleSolution
from models.sql import SqlExerciseType, SqlExTag, SqlExercise, SqlExerciseContent

sql_coll_1_ex_5: SqlExercise = SqlExercise(
    id=5,
    collectionId=1,
    toolId='sql',
    title='Anzahl der Untergebenen',
    authors=['bje40dc'],
    text="""Wie viele Untergebene hat jeder Chef? Geben Sie jeweils die OID des Chefs und die Anzahl aus!""",
    topics=[],
    difficulty=2,
    content=SqlExerciseContent(
        exerciseType=SqlExerciseType.SELECT,
        sampleSolutions=[
            SampleSolution(
                id=1,
                sample=dedent(
                    """\
                    SELECT chef_id, count(id)
                        FROM employee
                        WHERE chef_id IS NOT NULL
                        GROUP BY chef_id;"""
                )
            )
        ],
        tags=[SqlExTag.SQL_GROUP_BY]
    )
)
