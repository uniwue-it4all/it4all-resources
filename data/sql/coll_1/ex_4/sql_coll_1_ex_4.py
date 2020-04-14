from textwrap import dedent

from models.collection import ExerciseState, Exercise, SampleSolution, SemanticVersion
from models.sql import SqlExerciseContent, SqlExerciseType, SqlExerciseTag

sql_coll_1_ex_4 = Exercise(
    id=4,
    collectionId=1,
    toolId='sql',
    semanticVersion=SemanticVersion(major=1, minor=0, patch=0),
    title='Nutzernamen',
    authors=['bje40dc'],
    text='Geben Sie die Nutzernamen aller Angestellten alphabetisch geordnet aus!',
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
                    SELECT username
                        FROM employee
                        ORDER BY username;"""
                )
            )
        ],
        tags=[SqlExerciseTag.SQL_ORDER_BY]
    )
)
