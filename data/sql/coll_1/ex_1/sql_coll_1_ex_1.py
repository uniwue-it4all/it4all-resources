from textwrap import dedent

from models.collection import ExerciseState, Exercise, SemanticVersion, SampleSolution
from models.sql import SqlExerciseContent, SqlExerciseType

sql_coll_1_ex_1 = Exercise(
    id=1,
    collectionId=1,
    toolId='sql',
    semanticVersion=SemanticVersion(major=1, minor=0, patch=0),
    title='Anzahl der Angestellten',
    authors=['bje40dc'],
    text="""Wie viele Angestellte hat die Firma? Benennen Sie das Ergebnis als 'Anzahl'.""",
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
                    SELECT COUNT(*) AS Anzahl
                    FROM employee;"""
                )
            ),
            SampleSolution(
                id=2,
                sample=dedent(
                    """\
                    SELECT COUNT(id) AS Anzahl
                    FROM employee;"""
                )
            )
        ]
    )
)
