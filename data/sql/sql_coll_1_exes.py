from textwrap import dedent

from models.basics import SampleSolution
from models.sql import SqlExerciseContent, SqlExercise, SqlExerciseType, SqlExTag

sql_coll_1_ex_1 = SqlExercise(
    exerciseId=1,
    collectionId=1,
    toolId='sql',
    title='Anzahl der Angestellten',
    authors=['bje40dc'],
    text="""Wie viele Angestellte hat die Firma? Benennen Sie das Ergebnis als 'Anzahl'.""",
    difficulty=1,
    topicAbbreviations=[],
    content=SqlExerciseContent(
        exerciseType=SqlExerciseType.SELECT,
        schemaName='employee',
        sampleSolutions=[
            SampleSolution(
                id=1,
                sample=dedent(
                    """\
                    SELECT COUNT(*) AS Anzahl
                    FROM employee;"""
                )
            ),
            SampleSolution(
                id=2,
                sample=dedent(
                    """\
                    SELECT COUNT(id) AS Anzahl
                    FROM employee;"""
                )
            )
        ]
    )
)

sql_coll_1_ex_2 = SqlExercise(
    exerciseId=2,
    collectionId=1,
    toolId='sql',
    title='Angestelltennummer',
    authors=['bje40dc'],
    text="""Welche Angestelltennummer (id) hat Max Becker?""",
    difficulty=1,
    topicAbbreviations=[],
    content=SqlExerciseContent(
        exerciseType=SqlExerciseType.SELECT,
        schemaName='employee',
        sampleSolutions=[
            SampleSolution(
                id=1,
                sample=dedent(
                    """\
                    SELECT id
                        FROM employee
                        WHERE firstname = 'Max' AND lastname = 'Becker';"""
                )
            )
        ]
    )
)

sql_coll_1_ex_3 = SqlExercise(
    exerciseId=3,
    collectionId=1,
    toolId='sql',
    title='Emailadresse',
    authors=['bje40dc'],
    text='Welche Emailadresse hat Max Becker für die Arbeit?',
    difficulty=1,
    topicAbbreviations=[],
    content=SqlExerciseContent(
        exerciseType=SqlExerciseType.SELECT,
        schemaName='employee',
        sampleSolutions=[
            SampleSolution(
                id=1,
                sample=dedent(
                    """\
                    SELECT emailaddress
                        FROM employee JOIN emailaddress ON employee.id = emailaddress.employee_id
                        WHERE firstname = 'Max' AND lastname = 'Becker';"""
                )
            ),
            SampleSolution(
                id=2,
                sample=dedent(
                    """\
                    SELECT emailaddress
                        FROM employee, emailaddress
                        WHERE employee.id = emailaddress.employee_id AND firstname = 'Max' AND lastname = 'Becker';"""
                )
            ),
            SampleSolution(
                id=3,
                sample=dedent(
                    """\
                    SELECT emailaddress
                        FROM employee as emp, emailaddress as email
                        WHERE emp.id = email.employee_id AND firstname = 'Max' AND lastname = 'Becker';"""
                )
            )
        ],
        tags=[SqlExTag.SQL_JOIN]
    )
)

sql_coll_1_ex_4 = SqlExercise(
    exerciseId=4,
    collectionId=1,
    toolId='sql',
    title='Nutzernamen',
    authors=['bje40dc'],
    text='Geben Sie die Nutzernamen aller Angestellten alphabetisch geordnet aus!',
    difficulty=1,
    topicAbbreviations=[],
    content=SqlExerciseContent(
        exerciseType=SqlExerciseType.SELECT,
        schemaName='employee',
        sampleSolutions=[
            SampleSolution(
                id=1,
                sample=dedent(
                    """\
                    SELECT username
                        FROM employee
                        ORDER BY username;"""
                )
            )
        ],
        tags=[SqlExTag.SQL_ORDER_BY]
    )
)

sql_coll_1_ex_5 = SqlExercise(
    exerciseId=5,
    collectionId=1,
    toolId='sql',
    title='Anzahl der Untergebenen',
    authors=['bje40dc'],
    text="""Wie viele Untergebene hat jeder Chef? Geben Sie jeweils die OID des Chefs und die Anzahl aus!""",
    difficulty=2,
    topicAbbreviations=[],
    content=SqlExerciseContent(
        exerciseType=SqlExerciseType.SELECT,
        schemaName='employee',
        sampleSolutions=[
            SampleSolution(
                id=1,
                sample=dedent(
                    """\
                    SELECT chef_id, count(id)
                        FROM employee
                        WHERE chef_id IS NOT NULL
                        GROUP BY chef_id;"""
                )
            )
        ],
        tags=[SqlExTag.SQL_GROUP_BY]
    )
)

sql_coll_1_ex_6 = SqlExercise(
    exerciseId=6,
    collectionId=1,
    toolId='sql',
    title="""Tabelle 'employee' erstellen""",
    authors=['bje40dc'],
    text='Erstellen Sie das CREATE TABLE-Skript für die Tabelle employee!',
    topicAbbreviations=[],
    difficulty=2,
    content=SqlExerciseContent(
        exerciseType=SqlExerciseType.CREATE,
        schemaName='employee',
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

sql_coll_1_ex_7 = SqlExercise(
    exerciseId=7,
    collectionId=1,
    toolId='sql',
    title='Versetzung',
    authors=['bje40dc'],
    text=dedent(
        """\
        Der Angestellte mit der OID 8 arbeitet jetzt für den Angestellten mit der OID 3.
        Aktualisieren Sie die Datenbank!"""
    ).replace('\n', ' '),
    topics=[],
    difficulty=1,
    content=SqlExerciseContent(
        exerciseType=SqlExerciseType.UPDATE,
        schemaName='employee',
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

sql_coll_1_ex_8 = SqlExercise(
    exerciseId=8,
    collectionId=1,
    toolId='sql',
    title='Kündigung',
    authors=['bje40dc'],
    text="""Der Angestellte mit der OID 7 hat gekündigt. Löschen Sie ihn aus der Angestelltentabelle.""",
    topics=[],
    difficulty=1,
    content=SqlExerciseContent(
        exerciseType=SqlExerciseType.DELETE,
        schemaName='employee',
        sampleSolutions=[
            SampleSolution(
                id=1,
                sample=dedent(
                    """\
                    DELETE FROM employee
                        WHERE id = 7;"""
                )
            )
        ]
    )
)

sql_coll_1_ex_9 = SqlExercise(
    exerciseId=9,
    collectionId=1,
    toolId='sql',
    title='Neue Kollegin',
    authors=['bje40dc'],
    text=dedent(
        """\
        Es gibt eine neue Angestellte mit Namen Tina Sattler.
        Diese arbeitet für die Person mit der OID 2 und soll als OID 9 und als Nutzernamen 'tina_sattler' bekommen."""
    ),
    topics=[],
    difficulty=1,
    content=SqlExerciseContent(
        exerciseType=SqlExerciseType.INSERT,
        schemaName='employee',
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
        ],
    )
)

sql_coll_1_exes = [
    sql_coll_1_ex_1, sql_coll_1_ex_2, sql_coll_1_ex_3, sql_coll_1_ex_4, sql_coll_1_ex_5,
    sql_coll_1_ex_6, sql_coll_1_ex_7, sql_coll_1_ex_8, sql_coll_1_ex_9
]
