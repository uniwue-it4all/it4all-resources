from textwrap import dedent

from models.collection import SampleSolution
from models.sql import SqlExerciseType, SqlExercise

sql_coll_1_ex_6: SqlExercise = SqlExercise(
    id=6,
    collectionId=1,
    toolId='sql',
    title="""Tabelle 'employee' erstellen""",
    authors=['bje40dc'],
    text='Erstellen Sie das CREATE TABLE-Skript für die Tabelle employee!',
    topics=[],
    difficulty=2,
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
