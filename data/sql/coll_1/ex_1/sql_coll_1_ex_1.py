from textwrap import dedent

from models.collection import SampleSolution
from models.sql import SqlExerciseType, SqlExercise, SqlExerciseContent

sql_coll_1_ex_1: SqlExercise = SqlExercise(
    id=1,
    collectionId=1,
    toolId='sql',
    title='Anzahl der Angestellten',
    authors=['bje40dc'],
    text="""Wie viele Angestellte hat die Firma? Benennen Sie das Ergebnis als 'Anzahl'.""",
    topics=[],
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
