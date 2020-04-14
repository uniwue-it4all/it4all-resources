from textwrap import dedent

from models.collection import ExerciseState, Exercise, SampleSolution, SemanticVersion
from models.sql import SqlExerciseType, SqlExerciseContent

sql_coll_1_ex_8 = Exercise(
    id=8,
    collectionId=1,
    toolId='sql',
    semanticVersion=SemanticVersion(major=1, minor=0, patch=0),
    title='Kündigung',
    authors=['bje40dc'],
    text="""Der Angestellte mit der OID 7 hat gekündigt. Löschen Sie ihn aus der Angestelltentabelle.""",
    tags=[],
    state=ExerciseState.APPROVED,
    difficulty=1,
    content=SqlExerciseContent(
        exerciseType=SqlExerciseType.DELETE,
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
