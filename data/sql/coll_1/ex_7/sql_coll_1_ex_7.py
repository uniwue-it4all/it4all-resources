from textwrap import dedent

from models.collection import SampleSolution
from models.sql import SqlExerciseType, SqlExercise, SqlExerciseContent

sql_coll_1_ex_7: SqlExercise = SqlExercise(
    id=7,
    collectionId=1,
    toolId='sql',
    title='Versetzung',
    authors=['bje40dc'],
    text=dedent(
        """\
        Der Angestellte mit der OID 8 arbeitet jetzt für den Angestellten mit der OID 3.
        Aktualisieren Sie die Datenbank!"""
    ).replace('\n', ' '),
    topics=[],
    difficulty=1,
    sampleSolutions=[
        SampleSolution(
            id=1,
            sample=dedent(
                """\
                UPDATE employee
                    SET chef_id = 3
                    WHERE id = 8;"""
            )
        )
    ],
    content=SqlExerciseContent(
        exerciseType=SqlExerciseType.UPDATE,
    )
)
