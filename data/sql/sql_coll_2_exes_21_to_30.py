from textwrap import dedent

from models.basics import SampleSolution
from models.sql import SqlExerciseType, SqlExercise, SqlExerciseContent, SqlExTag

schemaName = 'amazon'

sql_coll_2_ex_21 = SqlExercise(
    exerciseId=21,
    collectionId=2,
    toolId="sql",
    title="Sterne in der Wüste 1",
    authors=["bje40dc"],
    text="""Wie oft wurde das Buch 'Die Stadt in der Wüste' bewertet? Nennen Sie die Spalte 'Anzahl'.""",
    topicAbbreviations=[],
    difficulty=2,
    content=SqlExerciseContent(
        exerciseType=SqlExerciseType.SELECT,
        schemaName=schemaName,
        sampleSolutions=[
            SampleSolution(
                id=1,
                sample=dedent(
                    """\
                    SELECT COUNT(*) AS Anzahl
                        FROM ratings JOIN books ON books.id = ratings.book_id
                        WHERE title = 'Die Stadt in der Wüste';"""
                )
            )
        ],
        tags=[SqlExTag.SQL_FUNCTION, SqlExTag.SQL_JOIN, SqlExTag.SQL_ALIAS],
    )
)

sql_coll_2_ex_22 = SqlExercise(
    exerciseId=22,
    collectionId=2,
    toolId="sql",
    title="Sterne in der Wüste 2",
    authors=["bje40dc"],
    text=dedent(
        """\
        Welche Durchschnittsbewertung bekam das Buch 'Die Stadt in der Wüste'?
        Nennen Sie die Spalte 'Durchschnitt'."""
    ).replace("\n", " "),
    topicAbbreviations=[],
    difficulty=1,
    content=SqlExerciseContent(
        exerciseType=SqlExerciseType.SELECT,
        schemaName=schemaName,
        sampleSolutions=[
            SampleSolution(
                id=1,
                sample=dedent(
                    """\
                    SELECT AVG(rating) AS Durchschnitt
                        FROM ratings JOIN books ON books.id = ratings.book_id
                        WHERE title = 'Die Stadt in der Wüste';"""
                )
            )
        ],
        tags=[SqlExTag.SQL_FUNCTION, SqlExTag.SQL_JOIN, SqlExTag.SQL_ALIAS]
    )
)

sql_coll_2_ex_23 = SqlExercise(
    exerciseId=23,
    collectionId=2,
    toolId="sql",
    title="Harry Potters",
    authors=["bje40dc"],
    text="""Wie hoch ist der Gesamtbestand an Harry Potter-Büchern? Nennen Sie die Spalte 'Gesamtbestand'.""",
    topicAbbreviations=[],
    difficulty=1,
    content=SqlExerciseContent(
        exerciseType=SqlExerciseType.SELECT,
        schemaName=schemaName,
        sampleSolutions=[
            SampleSolution(
                id=1,
                sample=dedent(
                    """\
                    SELECT SUM(stock) AS Gesamtbestand
                        FROM books
                        WHERE title like 'Harry Potter%';"""
                )
            )
        ],
        tags=[SqlExTag.SQL_FUNCTION, SqlExTag.SQL_ALIAS]
    )
)

sql_coll_2_ex_24 = SqlExercise(
    exerciseId=24,
    collectionId=2,
    toolId="sql",
    title="Fan oder nicht?",
    authors=["bje40dc"],
    text=dedent(
        """\
        Geben Sie jeweils die schlechteste und beste Bewertung des Buches 'Harry Potter und der Halbblutprinz' aus.
        Nennen Sie die Spalten jeweils 'Schlechteste' und 'Beste'."""
    ).replace("\n", " "),
    topicAbbreviations=[],
    difficulty=1,
    content=SqlExerciseContent(
        exerciseType=SqlExerciseType.SELECT,
        schemaName=schemaName,
        sampleSolutions=[
            SampleSolution(
                id=1,
                sample=dedent(
                    """\
                    SELECT min(rating) AS Schlechteste, max(rating) AS Beste
                        FROM books JOIN ratings ON books.id = ratings.book_id
                        WHERE title = 'Harry Potter und der Halbblutprinz';"""
                )
            )
        ],
        tags=[SqlExTag.SQL_FUNCTION, SqlExTag.SQL_ALIAS, SqlExTag.SQL_JOIN]
    )
)

sql_coll_2_ex_25 = SqlExercise(
    exerciseId=25,
    collectionId=2,
    toolId="sql",
    title="Durchschnittlicher Bestand",
    authors=["bje40dc"],
    text="""Wie hoch ist der durchschnittliche Bestand aller Bücher? Nennen Sie die Spalte 'Durchschnitt'.""",
    topicAbbreviations=[],
    difficulty=1,
    content=SqlExerciseContent(
        exerciseType=SqlExerciseType.SELECT,
        schemaName=schemaName,
        sampleSolutions=[
            SampleSolution(
                id=1,
                sample=dedent(
                    """\
                    SELECT AVG(stock) AS Durchschnitt
                    FROM books;""")
            )
        ],
        tags=[SqlExTag.SQL_FUNCTION, SqlExTag.SQL_ALIAS]
    )
)

sql_coll_2_ex_26 = SqlExercise(
    exerciseId=26,
    collectionId=2,
    toolId="sql",
    title="Wunsch des Phönix",
    authors=["bje40dc"],
    text="""Wie lauten die Nachnamen der Kunden die sich das Buch 'Harry Potter und der Orden des Phönix' wünschen?""",
    topicAbbreviations=[],
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
                    FROM customers
                      JOIN wishlists ON wishlists.customer_id = customers.id
                      JOIN books on wishlists.book_id = books.id
                    WHERE title = 'Harry Potter und der Orden des Phönix';"""
                )
            )
        ],
        tags=[SqlExTag.SQL_DOUBLE_JOIN]
    )
)

sql_coll_2_ex_27 = SqlExercise(
    exerciseId=27,
    collectionId=2,
    toolId="sql",
    title="Orwellianisch",
    authors=["bje40dc"],
    text=dedent(
        """\
        Suchen Sie die Titel aller Bücher, deren Autor George Orwell ist.
        Ordnen Sie die Titel nach Erscheinungsjahr abwärts."""
    ).replace("\n", " "),
    topicAbbreviations=[],
    difficulty=3,
    content=SqlExerciseContent(
        exerciseType=SqlExerciseType.SELECT,
        schemaName=schemaName,
        sampleSolutions=[
            SampleSolution(
                id=1,
                sample=dedent(
                    """\
                    SELECT title
                        FROM books JOIN authors on books.author_id = authors.id
                        WHERE first_name = 'George' AND family_name = 'Orwell'
                        ORDER BY year DESC;"""
                )
            )
        ],
        tags=[SqlExTag.SQL_ORDER_BY, SqlExTag.SQL_JOIN]
    )
)

sql_coll_2_ex_28 = SqlExercise(
    exerciseId=28,
    collectionId=2,
    toolId="sql",
    title="Teuer, teuer und teuer",
    authors=["bje40dc"],
    text=dedent(
        """\
        Zeigen sie Titel und Autor-ID der drei teuersten Bücher an.
        Sortieren Sie die Einträge nach Preis abwärts."""
    ).replace("\n", " "),
    topicAbbreviations=[],
    difficulty=2,
    content=SqlExerciseContent(
        exerciseType=SqlExerciseType.SELECT,
        schemaName=schemaName,
        sampleSolutions=[
            SampleSolution(
                id=1,
                sample=dedent(
                    """\
                    SELECT title, author_id
                        FROM books
                        ORDER BY price DESC
                        LIMIT 3;"""
                )
            )
        ],
        tags=[SqlExTag.SQL_ORDER_BY, SqlExTag.SQL_LIMIT]
    )
)

sql_coll_2_ex_29 = SqlExercise(
    exerciseId=29,
    collectionId=2,
    toolId="sql",
    title="Wer will Harry?",
    authors=["bje40dc"],
    text=dedent(
        """\
        Wählen Sie alle Bestellungen aus, die das Buch 'Harry Potter und der Halbblutprinz' enthalten.
        Geben Sie für diese Bestellungen jeweils das Datum und die Anzahl der bestellten Exemplare des Buches aus."""
    ).replace("\n", " "),
    topicAbbreviations=[],
    difficulty=2,
    content=SqlExerciseContent(
        exerciseType=SqlExerciseType.SELECT,
        schemaName=schemaName,
        sampleSolutions=[
            SampleSolution(
                id=1,
                sample=dedent(
                    """\
                    SELECT date, amount
                        FROM orders JOIN order_positions ON orders.id = order_id JOIN books ON books.id = book_id
                        WHERE title = 'Harry Potter und der Halbblutprinz';"""
                )
            )
        ],
        tags=[SqlExTag.SQL_DOUBLE_JOIN]
    )
)

sql_coll_2_ex_30 = SqlExercise(
    exerciseId=30,
    collectionId=2,
    toolId="sql",
    title="Emails mit G",
    authors=["bje40dc"],
    text="""Geben Sie alle Email-Adressen der Kunden aus die mit 'gmx.de ' oder mit 'gmail.com' enden.""",
    topicAbbreviations=[],
    difficulty=1,
    content=SqlExerciseContent(
        exerciseType=SqlExerciseType.SELECT,
        schemaName=schemaName,
        sampleSolutions=[
            SampleSolution(
                id=1,
                sample=dedent(
                    """\
                    SELECT email
                        FROM customers
                        WHERE email LIKE '%gmx.de' OR email LIKE '%gmail.com';"""
                )
            )
        ]
    )
)

sql_coll_2_exes_21_to_30 = [
    sql_coll_2_ex_21, sql_coll_2_ex_22, sql_coll_2_ex_23, sql_coll_2_ex_24, sql_coll_2_ex_25,
    sql_coll_2_ex_26, sql_coll_2_ex_27, sql_coll_2_ex_28, sql_coll_2_ex_29, sql_coll_2_ex_30,
]
