from textwrap import dedent

from models.basics import SampleSolution
from models.sql import SqlExTag, SqlExerciseContent, SqlExercise, SqlExerciseType

schemaName = 'amazon'

sql_coll_2_ex_41 = SqlExercise(
    exerciseId=41,
    collectionId=2,
    toolId='sql',
    title="Kurzer Nachname",
    authors=["bje40edc"],
    text=dedent(
        """\
        Wählen Sie alle Kunden aus, deren Nachname nur aus vier Buchstaben besteht.
        Geben Sie nur den Vornamen und Nachnamen aus.
        Die Datensätze sollen nach dem Nachnamen alphabetisch sortiert werden."""
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
                    SELECT first_name, family_name
                        FROM customers
                        WHERE LENGTH(family_name) = 4
                        ORDER BY family_name;"""
                )
            )
        ],
        tags=[SqlExTag.SQL_ORDER_BY]
    )
)

sql_coll_2_ex_42 = SqlExercise(
    exerciseId=42,
    collectionId=2,
    toolId='sql',
    title='Nachbestellen?',
    authors=['bje40dc'],
    text=dedent(
        """\
        Zeigen Sie Titel, Verlag-Name und Lagerbestand sämtlicher Bücher an,
        deren Lagerbestand geringer als 40000 ist."""
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
                    SELECT title, publishers.name, stock
                        FROM books JOIN publishers ON publisher_id = publishers.id
                        WHERE stock < 40000;"""
                )
            )
        ],
        hint="""Die Zuordnung von Verlag-Id zu Verlag-Name befindet sich in der Tabelle 'publishers'.""",
        tags=[SqlExTag.SQL_JOIN]
    )
)

sql_coll_2_ex_43 = SqlExercise(
    exerciseId=43,
    collectionId=2,
    toolId="sql",
    title="Neuer Kunde",
    authors=["bje40dc"],
    text=dedent(
        """\
        Fügen Sie einen neuen Kunden in die Datenbank ein. Name 'Ferdinandus Merkle', Email: 'ferdinandus_1856 @yahoo.com', Geburtstag: '1990 - 11 - 24 '. Das Passwort und die Adresse soll vorerst leer gelassen werden.
        """
    ).replace("\n", " "),
    topicAbbreviations=[],
    difficulty=2,
    content=SqlExerciseContent(
        exerciseType=SqlExerciseType.INSERT,
        schemaName=schemaName,
        sampleSolutions=[
            SampleSolution(
                id=1,
                sample=dedent(
                    """\
                    INSERT INTO customers (first_name, family_name, birthday, email, password, address)
                    VALUES ('Ferdinandus', 'Merkle', '1990 - 11 - 24', 'ferdinandus_1856 @yahoo.com','','');
                    """
                )
            ),
            SampleSolution(
                id=2,
                sample=dedent(
                    """\
                    INSERT INTO customers (first_name, family_name, birthday, email)
                    VALUES ('Ferdinandus', 'Merkle', '1990 - 11 - 24', 'ferdinandus_1856 @yahoo.com');"""
                )
            )
        ]
    )
)

sql_coll_2_ex_44 = SqlExercise(
    exerciseId=44,
    collectionId=2,
    toolId="sql",
    title="Immer diese Jugendlichen",
    authors=["bje40dc"],
    text="Löschen Sie alle Kunden, die nach dem Jahr 1995 geboren wurden.",
    topicAbbreviations=[],
    difficulty=2,
    content=SqlExerciseContent(
        exerciseType=SqlExerciseType.DELETE,
        schemaName=schemaName,
        sampleSolutions=[
            SampleSolution(
                id=1,
                sample=dedent(
                    """\
                    DELETE FROM customers
                        WHERE birthday > '1995-01-01';"""
                )
            )
        ]
    )
)

sql_coll_2_ex_45 = SqlExercise(
    exerciseId=45,
    collectionId=2,
    toolId="sql",
    title="Karteileichen",
    authors=["bje40dc"],
    text="Löschen Sie alle Kunden, die noch keine Bestellung abgegeben haben.",
    topicAbbreviations=[],
    difficulty=3,
    content=SqlExerciseContent(
        exerciseType=SqlExerciseType.DELETE,
        schemaName=schemaName,
        sampleSolutions=[
            SampleSolution(
                id=1,
                sample=dedent(
                    """\
                    DELETE FROM customers
                        WHERE id NOT IN (SELECT customer_id FROM orders);"""
                )
            )
        ],
        hint="Verwenden Sie den Operator 'IN' für diese Aufgabe."
    )
)

sql_coll_2_ex_46 = SqlExercise(
    exerciseId=46,
    collectionId=2,
    toolId="sql",
    title="Weg mit den Billigheimern",
    authors=["bje40dc"],
    text="Löschen Sie alle Bücher, die mehr als 8,50 Euro kosten und die Verlags-ID 7 besitzen.",
    topicAbbreviations=[],
    difficulty=1,
    content=SqlExerciseContent(
        exerciseType=SqlExerciseType.DELETE,
        schemaName=schemaName,
        sampleSolutions=[
            SampleSolution(
                id=1,
                sample=dedent(
                    """\
                    DELETE FROM books
                        WHERE price > 8.50 AND publisher_id = '7';"""
                )
            )
        ]
    )
)

sql_coll_2_ex_47 = SqlExercise(
    exerciseId=47,
    collectionId=2,
    toolId="sql",
    title="Bye Bye, J. R. R!",
    authors=["bje40dc"],
    text="Löschen Sie alle Bücher, die vom Autor mit der ID 3 geschrieben wurden.",
    topicAbbreviations=[],
    difficulty=3,
    content=SqlExerciseContent(
        exerciseType=SqlExerciseType.DELETE,
        schemaName=schemaName,
        sampleSolutions=[
            SampleSolution(
                id=1,
                sample=dedent(
                    """\
                    DELETE FROM books
                        WHERE author_id = 3;"""
                )
            )
        ]
    )
)

sql_coll_2_ex_48 = SqlExercise(
    exerciseId=48,
    collectionId=2,
    toolId="sql",
    title="Neues Buch",
    authors=["bje40dc"],
    text=dedent(
        """\
        Fügen Sie ein neues Buch mit dem Titel 'Applied Statistical Genetics with R ' in die Datenbank ein
        (Autor-ID: 2, Erscheinungsjahr: 2010, Publisher-ID: '12' , Signatur 'PF / 520 - Y / 2',
        Lagerbestand '289', Preis: '24.99 ')."""
    ).replace("\n", " "),
    topicAbbreviations=[],
    difficulty=2,
    content=SqlExerciseContent(
        exerciseType=SqlExerciseType.INSERT,
        schemaName=schemaName,
        sampleSolutions=[
            SampleSolution(
                id=1,
                sample="""\
                INSERT INTO books (title, author_id, year, publisher_id, isbn, stock, price)
                    VALUES('Applied Statistical Genetics with R', 2, 2010, 12, 'PF/520-Y/2', 289, 24.99);"""
            )
        ]
    )
)

sql_coll_2_exes_41_to_50 = [
    sql_coll_2_ex_41, sql_coll_2_ex_42, sql_coll_2_ex_43, sql_coll_2_ex_44, sql_coll_2_ex_45,
    sql_coll_2_ex_46, sql_coll_2_ex_47, sql_coll_2_ex_48,
]
