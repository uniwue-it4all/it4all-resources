from textwrap import dedent

from models.collection import SampleSolution
from models.sql import SqlExerciseType, SqlExercise, SqlExerciseContent, SqlExTag

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

sql_coll_2_ex_11 = SqlExercise(
    exerciseId=11,
    collectionId=2,
    toolId="sql",
    title="""Wer schrieb was?""",
    authors=["bje40dc"],
    text=dedent(
        """\
        Ordnen Sie allen Büchern ihre jeweiligen Autoren zu.
        Geben Sie jeweils den Titel des Buches und den Nachnamen des Autoren aus!"""
    ).replace("\n", " "),
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
                    SELECT title, family_name
                        FROM authors JOIN books ON authors.id = books.author_id;"""
                )
            )
        ],
        tags=[SqlExTag.SQL_JOIN]
    )
)

sql_coll_2_ex_12 = SqlExercise(
    exerciseId=12,
    collectionId=2,
    toolId="sql",
    title="Bücher von Carlsen",
    authors=["bje40dc"],
    text="""Bestimmen Sie Titel und Preis aller Bücher die im Verlag 'Carlsen' erschienen sind.""",
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
                    SELECT title, price
                        FROM books JOIN publishers ON publisher_id = publishers.id
                        WHERE name = 'Carlsen';"""
                )
            )
        ],
        tags=[SqlExTag.SQL_JOIN],
        hint="""Die Zuordnung von Verlag-Id zu Verlag-Name befindet sich in der Tabelle 'publishers'."""
    )
)

sql_coll_2_ex_13 = SqlExercise(
    exerciseId=13,
    collectionId=2,
    toolId="sql",
    title="Harry Potters Leben",
    authors=["bje40dc"],
    text="""Bestimmen Sie Titel und ISBN sämtlicher Bücher der Autorin 'Rowling' (ohne Anführungszeichen).""",
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
                    SELECT title, isbn
                        FROM books JOIN authors on books.author_id = authors.id
                        WHERE family_name = 'Rowling'"""
                )
            )
        ],
        tags=[SqlExTag.SQL_JOIN]
    )
)

sql_coll_2_ex_14 = SqlExercise(
    exerciseId=14,
    collectionId=2,
    toolId="sql",
    title="Wilhards Wertungen",
    authors=["bje40dc"],
    text="""Zeigen Sie die Werte aller Ratings an, die der Kunde mit der Email 'wilhard_1041@web.de' abgegeben hat.""",
    topics=[],
    difficulty=2,
    content=SqlExerciseContent(
        exerciseType=SqlExerciseType.SELECT,
        schemaName=schemaName,
        sampleSolutions=[
            SampleSolution(
                id=1,
                sample=dedent(
                    """\
                    SELECT rating
                        FROM ratings JOIN customers ON ratings.customer_id = customers.id
                        WHERE email = 'wilhard_1041@web.de';"""
                )
            )
        ],
        tags=[SqlExTag.SQL_JOIN]
    )
)

sql_coll_2_ex_15 = SqlExercise(
    exerciseId=15,
    collectionId=2,
    toolId="sql",
    title="""Wer hat hier so viel bestellt?""",
    authors=["bje40dc"],
    text="""Wie lauten die Nachnamen der Kunden, die mindestens 3 Bestellung aufgegeben haben?""",
    topics=[],
    difficulty=2,
    content=SqlExerciseContent(
        exerciseType=SqlExerciseType.SELECT,
        schemaName=schemaName,
        sampleSolutions=[
            SampleSolution(
                id=1,
                sample=dedent(
                    """\
                    SELECT DISTINCT family_name
                        FROM orders JOIN customers ON orders.customer_id = customers.id
                        WHERE orders.id >= 3;"""
                )
            )
        ],
        tags=[SqlExTag.SQL_JOIN],
        hint="""Diese Bestellungen haben eine ID von mindestens 3."""
    )
)

sql_coll_2_ex_16 = SqlExercise(
    exerciseId=16,
    collectionId=2,
    toolId="sql",
    title="GMX-Kunden",
    authors=["bje40dc"],
    text="""Geben Sie alle Email-Adressen der Kunden aus die mit 'gmx.de' enden.""",
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
                    SELECT email
                        FROM customers
                        WHERE email LIKE '%gmx.de';"""
                )
            )
        ],
        hint="""Verwenden Sie für die Eingrenzung der Mailadresse den 'LIKE'-Operator."""
    )
)

sql_coll_2_ex_17 = SqlExercise(
    exerciseId=17,
    collectionId=2,
    toolId="sql",
    title="Billige Bücher",
    authors=["bje40dc"],
    text="""Geben Sie die Titel aller Bücher aus die weniger als 10,00 € kosten.""",
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
                        FROM books WHERE price < 10.00;"""
                )
            )
        ]
    )
)

sql_coll_2_ex_18 = SqlExercise(
    exerciseId=18,
    collectionId=2,
    toolId="sql",
    title="Was wird gewünscht?",
    authors=["bje40dc"],
    text=dedent(
        """\
        Geben die die IDs aller Bücher aus, die von Kunden gewünscht werden.
        Achten Sie darauf, dass eine ID nur einmal vorkommt."""
    ),
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
                    SELECT DISTINCT book_id
                        FROM wishlists;"""
                )
            )
        ]
    )
)

sql_coll_2_ex_19 = SqlExercise(
    exerciseId=19,
    collectionId=2,
    toolId="sql",
    title="Jahrgang 81",
    authors=["bje40dc"],
    text="""Wählen Sie die Vor- und Nachnamen der Kunden aus, die im Jahr 1981 Geburtstag haben.""",
    topics=[],
    difficulty=2,
    content=SqlExerciseContent(
        exerciseType=SqlExerciseType.SELECT,
        schemaName=schemaName,
        sampleSolutions=[
            SampleSolution(
                id=1,
                sample=dedent(
                    """\
                    SELECT first_name, family_name
                        FROM customers
                        WHERE birthday < '1982-01-01' AND birthday > '1980-12-31';"""
                )
            ),
            SampleSolution(
                id=2,
                sample=dedent(
                    """\
                    SELECT first_name, family_name
                        FROM customers
                        WHERE birthday LIKE '1981-%';"""
                )
            )
        ],
        hint="""Verwenden Sie den 'LIKE'-Operator zu Vergleich des Jahres."""
    )
)

sql_coll_2_ex_20 = SqlExercise(
    exerciseId=20,
    collectionId=2,
    toolId="sql",
    title="Geringer Bestand oder Preis",
    authors=["bje40dc"],
    text=dedent(
        """\
        Geben Sie die Titel aller Bücher aus, die einen Bestand von weniger als 20.000 Exemplaren
        oder einen Preis unter 14€ haben."""
    ).replace("\n", " "),
    topics=[],
    difficulty=2,
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
                        WHERE stock < 20000 OR price < 14.00;"""
                )
            ),
            SampleSolution(
                id=2,
                sample=dedent(
                    """\
                    SELECT title
                        FROM books
                        WHERE stock < 20000 OR price < 14;"""
                )
            )
        ]
    )
)

sql_coll_2_ex_21 = SqlExercise(
    exerciseId=21,
    collectionId=2,
    toolId="sql",
    title="Sterne in der Wüste 1",
    authors=["bje40dc"],
    text="""Wie oft wurde das Buch 'Die Stadt in der Wüste' bewertet? Nennen Sie die Spalte 'Anzahl'.""",
    topics=[],
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
    topics=[],
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
    topics=[],
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
    topics=[],
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
                    SELECT email
                        FROM customers
                        WHERE email LIKE '%gmx.de' OR email LIKE '%gmail.com';"""
                )
            )
        ]
    )
)

sql_coll_2_exes = [
    sql_coll_2_ex_01, sql_coll_2_ex_02, sql_coll_2_ex_03, sql_coll_2_ex_04, sql_coll_2_ex_05,
    sql_coll_2_ex_06, sql_coll_2_ex_07, sql_coll_2_ex_08, sql_coll_2_ex_09, sql_coll_2_ex_10,
    sql_coll_2_ex_11, sql_coll_2_ex_12, sql_coll_2_ex_13, sql_coll_2_ex_14, sql_coll_2_ex_15,
    sql_coll_2_ex_16, sql_coll_2_ex_17, sql_coll_2_ex_18, sql_coll_2_ex_19, sql_coll_2_ex_20,
    sql_coll_2_ex_21, sql_coll_2_ex_22, sql_coll_2_ex_23, sql_coll_2_ex_24, sql_coll_2_ex_25,
    sql_coll_2_ex_26, sql_coll_2_ex_27, sql_coll_2_ex_28, sql_coll_2_ex_29, sql_coll_2_ex_30,
]
