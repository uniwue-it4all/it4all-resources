from textwrap import dedent

from models.collection import ExerciseState, Exercise, SampleSolution, SemanticVersion
from models.sql import SqlExerciseType, SqlExerciseContent

sql_coll_1_ex_9 = Exercise(
    id=9,
    collectionId=1,
    toolId='sql',
    semanticVersion=SemanticVersion(major=1, minor=0, patch=0),
    title='Neue Kollegin',
    authors=['bje40dc'],
    text=dedent(
        """\
        Es gibt eine neue Angestellte mit Namen Tina Sattler.
        Diese arbeitet für die Person mit der OID 2 und soll als OID 9 und als Nutzernamen 'tina_sattler' bekommen."""
    ),
    tags=[],
    state=ExerciseState.APPROVED,
    difficulty=1,
    content=SqlExerciseContent(
        exerciseType=SqlExerciseType.INSERT,
        sampleSolutions=[
            SampleSolution(
                id=1,
                sample="""INSERT INTO employee VALUES (9, 'Tina', 'Sattler', 'tina_sattler', 2);"""
            ),
            SampleSolution(
                id=2,
                sample=dedent(
                    """\
                    INSERT INTO employee (id, firstname, lastname, username, chef_id)
                    VALUES (9, 'Tina', 'Sattler', 'tina_sattler', 2);"""
                )
            )
        ]
    )
)
