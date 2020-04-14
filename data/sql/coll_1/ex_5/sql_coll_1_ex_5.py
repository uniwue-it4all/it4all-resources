from textwrap import dedent

from models.collection import ExerciseState, Exercise, SampleSolution, SemanticVersion
from models.sql import SqlExerciseType, SqlExerciseContent, SqlExerciseTag

sql_coll_1_ex_5 = Exercise(
    id=5,
    collectionId=1,
    toolId='sql',
    semanticVersion=SemanticVersion(major=1, minor=0, patch=0),
    title='Anzahl der Untergebenen',
    authors=['bje40dc'],
    text="""Wie viele Untergebene hat jeder Chef? Geben Sie jeweils die OID des Chefs und die Anzahl aus!""",
    tags=[],
    state=ExerciseState.APPROVED,
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
        tags=[SqlExerciseTag.SQL_GROUP_BY]
    )
)
