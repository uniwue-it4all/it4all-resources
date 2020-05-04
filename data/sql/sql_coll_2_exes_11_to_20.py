from textwrap import dedent

from models.basics import SampleSolution
from models.sql import SqlExerciseType, SqlExercise, SqlExerciseContent, SqlExTag

schemaName = "amazon"

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

sql_coll_2_exes_11_to_20 = [
    sql_coll_2_ex_11, sql_coll_2_ex_12, sql_coll_2_ex_13, sql_coll_2_ex_14, sql_coll_2_ex_15,
    sql_coll_2_ex_16, sql_coll_2_ex_17, sql_coll_2_ex_18, sql_coll_2_ex_19, sql_coll_2_ex_20,
]
