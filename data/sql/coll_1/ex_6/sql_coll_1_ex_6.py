from textwrap import dedent

from models.collection import ExerciseState, Exercise, SampleSolution, SemanticVersion
from models.sql import SqlExerciseType, SqlExerciseContent, SqlExTag

sql_coll_1_ex_6: Exercise[SqlExTag, SqlExerciseContent] = Exercise(
    id=6,
    collectionId=1,
    toolId='sql',
    semanticVersion=SemanticVersion(major=1, minor=0, patch=0),
    title="""Tabelle 'employee' erstellen""",
    authors=['bje40dc'],
    text='Erstellen Sie das CREATE TABLE-Skript für die Tabelle employee!',
    tags=[],
    state=ExerciseState.CREATED,
    difficulty=2,
    content=SqlExerciseContent(
        exerciseType=SqlExerciseType.CREATE,
        sampleSolutions=[
            SampleSolution(
                id=1,
                sample=dedent(
                    """\
                    CREATE TABLE employee (
                        id INT PRIMARY KEY,
                        firstname VARCHAR(50),
                        lastname VARCHAR(50),
                        username VARCHAR(20),
                        chef_id INT,
                        FOREIGN KEY (chef_id) REFERENCES employee(id)
                  );"""
                )
            )
        ]
    )
)
