from textwrap import dedent

from models.collection import SampleSolution
from models.sql import SqlExerciseContent, SqlExerciseType, SqlExercise

schemaName = "amazon"

sql_coll_2_ex_01 = SqlExercise(
    exerciseId=1,
    collectionId=2,
    toolId="sql",
    title="Alles über die Autoren",
    authors=["bje40dc"],
    text="""Geben Sie alle Spalten der Autorentabelle aus!""",
    topics=[],
    difficulty=1,
    content=SqlExerciseContent(
        exerciseType=SqlExerciseType.SELECT,
        schemaName=schemaName,
        sampleSolutions=[
            SampleSolution(
                id=1,
                sample=dedent(
                    """\
                    SELECT *
                        FROM authors;"""
                )
            ),
            SampleSolution(
                id=2,
                sample=dedent(
                    """\
                    SELECT id, first_name, family_name, birthday
                        FROM authors;"""
                )
            )
        ]
    )
)

sql_coll_2_ex_02 = SqlExercise(
    exerciseId=2,
    collectionId=2,
    toolId="sql",
    title="Nachnamen aller Autoren",
    authors=["bje40dc"],
    text="""Geben Sie die Nachnamen aller Autoren aus!""",
    topics=[],
    difficulty=1,
    content=SqlExerciseContent(
        exerciseType=SqlExerciseType.SELECT,
        schemaName=schemaName,
        sampleSolutions=[
            SampleSolution(
                id=1,
                sample=dedent(
                    """\
                    SELECT family_name
                        FROM authors;"""
                )
            )
        ]
    )
)

sql_coll_2_ex_03 = SqlExercise(
    exerciseId=3,
    collectionId=2,
    toolId="sql",
    title="Verlagsnamen",
    authors=["bje40dc"],
    text="""Geben Sie die Namen aller Verlage aus!""",
    topics=[],
    difficulty=1,
    content=SqlExerciseContent(
        exerciseType=SqlExerciseType.SELECT,
        schemaName=schemaName,
        sampleSolutions=[
            SampleSolution(
                id=1,
                sample=dedent(
                    """\
                    SELECT name
                        FROM publishers;"""
                )
            )
        ]
    )
)

sql_coll_2_ex_04 = SqlExercise(
    exerciseId=4,
    collectionId=2,
    toolId="sql",
    title="Namen aller Kunden",
    authors=["bje40dc"],
    text="""Geben Sie die Vor- und Nachnamen aller Kunden aus!""",
    topics=[],
    difficulty=1,
    content=SqlExerciseContent(
        exerciseType=SqlExerciseType.SELECT,
        schemaName=schemaName,
        sampleSolutions=[
            SampleSolution(
                id=1,
                sample=dedent(
                    """\
                    SELECT first_name, family_name
                        FROM customers;"""
                )
            )
        ]
    )
)

sql_coll_2_ex_05 = SqlExercise(
    exerciseId=5,
    collectionId=2,
    toolId="sql",
    title="""Daten über Bücher""",
    authors=["bje40dc"],
    text="""Geben Sie für jedes Buch jeweils den Titel das Erscheinungsjahr und die ISBN aus!""",
    topics=[],
    difficulty=1,
    content=SqlExerciseContent(
        exerciseType=SqlExerciseType.SELECT,
        schemaName=schemaName,
        sampleSolutions=[
            SampleSolution(
                id=1,
                sample=dedent(
                    """\
                    SELECT title, year, isbn
                        FROM books;"""
                )
            )
        ]
    )
)

sql_coll_2_ex_06 = SqlExercise(
    exerciseId=6,
    collectionId=2,
    toolId="sql",
    title="""Titelsuche""",
    authors=["bje40dc"],
    text="""Bestimmen Sie den Titel des Buches mit der ISBN '978-3551354051' (ohne Anführungszeichen).""",
    topics=[],
    difficulty=1,
    content=SqlExerciseContent(
        exerciseType=SqlExerciseType.SELECT,
        schemaName=schemaName,
        sampleSolutions=[
            SampleSolution(
                id=1,
                sample=dedent(
                    """\
                    SELECT title
                        FROM books
                        WHERE isbn = '978-3551354051';"""
                )
            )
        ]
    )
)

sql_coll_2_ex_07 = SqlExercise(
    exerciseId=7,
    collectionId=2,
    toolId="sql",
    title="Preissuche",
    authors=["bje40dc"],
    text="Bestimmen Sie den Preis des Buches mit der ISBN '978-3551354068' (ohne Anführungszeichen).",
    topics=[],
    difficulty=1,
    content=SqlExerciseContent(
        exerciseType=SqlExerciseType.SELECT,
        schemaName=schemaName,
        sampleSolutions=[
            SampleSolution(
                id=1,
                sample=dedent(
                    """\
                    SELECT price
                        FROM books
                        WHERE isbn = '978-3551354068';"""
                )
            )
        ]
    )
)

sql_coll_2_ex_08 = SqlExercise(
    exerciseId=8,
    collectionId=2,
    toolId="sql",
    title="Autorensuche",
    authors=["bje40dc"],
    text="Bestimmen Sie den Vor- und Nachnamen des Autoren mit der ID 3.",
    topics=[],
    difficulty=1,
    content=SqlExerciseContent(
        exerciseType=SqlExerciseType.SELECT,
        schemaName=schemaName,
        sampleSolutions=[
            SampleSolution(
                id=1,
                sample=dedent(
                    """\
                    SELECT first_name, family_name
                        FROM authors
                        WHERE id = 3;"""
                )
            )
        ]
    )
)

sql_coll_2_ex_09 = SqlExercise(
    exerciseId=9,
    collectionId=2,
    toolId="sql",
    title="""Der kleine Prinz?""",
    authors=["bje40dc"],
    text="Bestimmen Sie die Autor-ID des Buches 'Der kleine Prinz' (ohne Anführungszeichen).",
    topics=[],
    difficulty=1,
    content=SqlExerciseContent(
        exerciseType=SqlExerciseType.SELECT,
        schemaName=schemaName,
        sampleSolutions=[
            SampleSolution(
                id=1,
                sample=dedent(
                    """\
                    SELECT author_id
                        FROM books
                        WHERE title = 'Der kleine Prinz';"""
                )
            )
        ]
    )
)

sql_coll_2_ex_10 = SqlExercise(
    exerciseId=10,
    collectionId=2,
    toolId="sql",
    title="Verlag mit Telefonnummer",
    authors=["bje40dc"],
    text="""Bestimmen Sie den Namen des Verlages der unter der Telefonnummer '+49 2402 / 806341' erreichbar ist.""",
    topics=[],
    difficulty=1,
    content=SqlExerciseContent(
        exerciseType=SqlExerciseType.SELECT,
        schemaName=schemaName,
        sampleSolutions=[
            SampleSolution(
                id=1,
                sample=dedent(
                    """\
                    SELECT name
                        FROM publishers
                        WHERE phone = '+49 2402 / 806341';"""
                )
            )
        ]
    )
)

sql_coll_2_exes_01_to_10 = [
    sql_coll_2_ex_01, sql_coll_2_ex_02, sql_coll_2_ex_03, sql_coll_2_ex_04, sql_coll_2_ex_05,
    sql_coll_2_ex_06, sql_coll_2_ex_07, sql_coll_2_ex_08, sql_coll_2_ex_09, sql_coll_2_ex_10
]
