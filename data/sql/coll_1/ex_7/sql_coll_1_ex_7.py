from textwrap import dedent

from models.collection import ExerciseState, Exercise, SampleSolution, SemanticVersion
from models.sql import SqlExerciseType, SqlExerciseContent

sql_coll_1_ex_7 = Exercise(
    id=7,
    collectionId=1,
    toolId='sql',
    semanticVersion=SemanticVersion(major=1, minor=0, patch=0),
    title='Versetzung',
    authors=['bje40dc'],
    text=dedent(
        """\
        Der Angestellte mit der OID 8 arbeitet jetzt für den Angestellten mit der OID 3.
        Aktualisieren Sie die Datenbank!"""
    ).replace('\n', ' '),
    tags=[],
    state=ExerciseState.APPROVED,
    difficulty=1,
    content=SqlExerciseContent(
        exerciseType=SqlExerciseType.UPDATE,
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
        ]
    )
)
