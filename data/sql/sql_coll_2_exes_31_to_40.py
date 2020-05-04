from textwrap import dedent

from models.collection import SampleSolution
from models.sql import SqlExerciseType, SqlExercise, SqlExerciseContent, SqlExTag

schemaName = "amazon"

sql_coll_2_ex_31 = SqlExercise(
    exerciseId=31,
    collectionId=2,
    toolId="sql",
    title="Tolkien in Billig",
    authors=["bje40dc"],
    text=dedent(
        """\
        Bestimmen Sie Titel und Preis aller Bücher des Autors 'Tolkien' deren Preis über 10€ liegt.
        Ordnen Sie die Einträge nach Erscheinungsjahr abwärts."""
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
                    SELECT title, price
                        FROM books JOIN authors on authors.id = books.author_id
                        WHERE authors.family_name = 'Tolkien' AND price > 10
                        ORDER BY year DESC;"""
                )
            )
        ],
        tags=[SqlExTag.SQL_ORDER_BY]
    )
)

sql_coll_2_ex_32 = SqlExercise(
    exerciseId=32,
    collectionId=2,
    toolId="sql",
    title="Billig gekauft",
    authors=["bje40dc"],
    text=dedent(
        """\
        Berechnen Sie die Anzahl der bestellten Buchexemplare (Tabelle order_positions), die zum Zeitpunkt des Kaufes
        weniger als fünf Euro gekostet haben. Geben Sie das Ergebnis unter dem Spaltenname 'Anzahl' aus."""
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
                    SELECT SUM(amount) AS Anzahl
                        FROM order_positions
                        WHERE price < 5;"""
                )
            ),
            SampleSolution(
                id=2,
                sample=dedent(
                    """\
                    SELECT SUM(amount) AS Anzahl
                        FROM order_positions
                        WHERE price < 5.00;"""
                )
            )
        ],
        tags=[SqlExTag.SQL_FUNCTION, SqlExTag.SQL_ALIAS]
    )
)

sql_coll_2_ex_33 = SqlExercise(
    exerciseId=33,
    collectionId=2,
    toolId="sql",
    title="Kumulierter Bestand",
    authors=["bje40dc"],
    text=dedent(
        """\
        Erfassen Sie die ID aller Autoren und den kumulierten Bestand ihrer Bücher.
        Ordnen Sie die Einträge nach kumulierten Bestand abwärts.
        Benennen Sie die Spalte des kumulierten Bestandes 'stock_sum' (ohne Anführungszeichen)."""
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
                    SELECT author_id, sum(stock) AS stock_sum
                        FROM books
                        GROUP BY author_id
                        ORDER BY stock_sum DESC;"""
                )
            )
        ],
        tags=[SqlExTag.SQL_FUNCTION, SqlExTag.SQL_GROUP_BY, SqlExTag.SQL_ORDER_BY],
        hint="""Verwenden Sie den Sum-Operator und das Schlüsselwort AS."""
    )
)

sql_coll_2_ex_34 = SqlExercise(
    exerciseId=34,
    collectionId=2,
    toolId="sql",
    title="Februargeburtstag",
    authors=["bje40dc"],
    text=dedent(
        """\
        Wählen Sie alle Kunden aus die im Februar Geburtstag haben und geben Sie den Vornamen,
        Nachnamen und das Geburtsdatum aus."""
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
                    SELECT first_name, family_name, birthday
                        FROM customers
                        WHERE birthday LIKE '%-02-%';"""
                )
            )
        ],
        hint="""Verwenden Sie für die Eingrenzung des Geburtsdatums den 'LIKE'-Operator."""
    )
)

sql_coll_2_ex_35 = SqlExercise(
    exerciseId=35,
    collectionId=2,
    toolId="sql",
    title="Ich bin der Jüngste!",
    authors=["bje40dc"],
    text="""Geben Sie den Vornamen, Nachnamen und Geburtstag des jüngsten Kunden aus.""",
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
                    SELECT first_name, family_name, birthday
                        FROM customers
                        ORDER BY birthday DESC
                        LIMIT 1;"""
                )
            )
        ],
        tags=[SqlExTag.SQL_ORDER_BY, SqlExTag.SQL_LIMIT],
        hint="Achten Sie darauf, dass sich die Spaltennamen nicht verändern."
    )
)

sql_coll_2_ex_36 = SqlExercise(
    exerciseId=36,
    collectionId=2,
    toolId="sql",
    title="Passwortupdate!",
    authors=["bje40dc"],
    text=dedent(
        """\
        Sie möchten ihre Kunden dazu motivieren sichere Passwörter zu verwenden.
        Alle Kunden, die als Kennwort 'Passwort' verwenden, sollen beim nächsten Login über eine Meldung aufgefordert
        werden, sich ein neues auszudenken.
        Geben Sie die ID und die Email-Adresse der faulen Kunden aus."""
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
                    SELECT id, email
                        FROM customers
                        WHERE password = '3e45af4ca27ea2b03fc6183af40ea112';"""
                )
            )
        ],
        hint=dedent(
            """\
            Die Passwörter der Kunden sind als MD5-Hash-String in der Tabelle 'customers' gespeichert.
            Der MD5-Hashstring zu 'Passwort' lautet '3e45af4ca27ea2b03fc6183af40ea112'."""
        )
    )
)

sql_coll_2_ex_37 = SqlExercise(
    exerciseId=37,
    collectionId=2,
    toolId="sql",
    title="Mit allem zufrieden?",
    authors=["bje40dc"],
    text=dedent(
        """\
        Ermitteln Sie den Kunden, welcher die höchste durchschnittliche Bewertung abgegeben hat.
        Geben Sie dazu Vorname, Nachname und seine durchschnittliche Bewertung (Spaltenbezeichnung 'avg_rating') aus."""
    ),
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
                    SELECT customers.first_name, customers.family_name, AVG(rating) AS avg_rating
                        FROM ratings LEFT JOIN customers ON customers.id = customer_id
                        GROUP BY customer_id
                        ORDER BY avg_rating DESC
                        LIMIT 1;"""
                )
            )
        ],
        tags=[SqlExTag.SQL_JOIN, SqlExTag.SQL_FUNCTION, SqlExTag.SQL_GROUP_BY, SqlExTag.SQL_ORDER_BY,
              SqlExTag.SQL_LIMIT]
    )
)

sql_coll_2_ex_38 = SqlExercise(
    exerciseId=38,
    collectionId=2,
    toolId="sql",
    title="Teure Wünsche...",
    authors=["bje40dc"],
    text=dedent(
        """\
        Ermitteln Sie den Einkaufswert der Wunschlisten für jeden Kunden.
        Listen Sie dabei Vorname, Nachname und Einkaufswert (Spaltenbezeichnung 'value') auf.
        Sortieren Sie die Einträge aufwärts nach Einkaufswert."""
    ).replace("\n", " "),
    topics=[],
    difficulty=4,
    content=SqlExerciseContent(
        exerciseType=SqlExerciseType.SELECT,
        schemaName=schemaName,
        sampleSolutions=[
            SampleSolution(
                id=1,
                sample=dedent(
                    """\
                    SELECT customers.first_name, customers.family_name, SUM(price) AS value
                        FROM wishlists
                            LEFT JOIN books ON books.id = book_id
                            LEFT JOIN customers ON customers.id = customer_id
                        GROUP BY customer_id
                        ORDER BY value;"""
                )
            )
        ],
        tags=[
            SqlExTag.SQL_FUNCTION, SqlExTag.SQL_ALIAS, SqlExTag.SQL_DOUBLE_JOIN, SqlExTag.SQL_GROUP_BY,
            SqlExTag.SQL_ORDER_BY
        ]
    )
)

sql_coll_2_ex_39 = SqlExercise(
    exerciseId=39,
    collectionId=2,
    toolId="sql",
    title="Veröffentlichungsjahre",
    authors=["bje40dc"],
    text="""Wählen Sie alle Bücher aus, die in den Jahren 1998, 2001 oder 2011 veröffentlicht wurden.""",
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
                    SELECT * FROM books
                        WHERE year IN (1998, 2001, 2011);"""
                )
            )
        ]
    )
)
sql_coll_2_ex_40 = SqlExercise(
    exerciseId=40,
    collectionId=2,
    toolId="sql",
    title="Aufgestockt",
    authors=["bje40dc"],
    text=dedent(
        """\
        Es sind neue Exemplare des Buches mit dem Titel 1894 eingetroffen.
        Aktualisieren Sie den Bestand auf den neuen Wert von 500."""
    ).replace("\n", " "),
    topics=[],
    difficulty=1,
    content=SqlExerciseContent(
        exerciseType=SqlExerciseType.UPDATE,
        schemaName=schemaName,
        sampleSolutions=[
            SampleSolution(
                id=1,
                sample=dedent(
                    """\
                    UPDATE books
                        SET stock = 500
                        WHERE title = '1984';"""
                )
            )
        ],
        tags=[SqlExTag.SQL_UPDATE]
    )
)
sql_coll_2_exes_31_to_40 = [
    sql_coll_2_ex_31, sql_coll_2_ex_32, sql_coll_2_ex_33, sql_coll_2_ex_34, sql_coll_2_ex_35,
    sql_coll_2_ex_36, sql_coll_2_ex_37, sql_coll_2_ex_38, sql_coll_2_ex_39, sql_coll_2_ex_40
]
