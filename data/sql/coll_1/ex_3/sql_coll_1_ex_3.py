from textwrap import dedent

from models.collection import SampleSolution
from models.sql import SqlExerciseType, SqlExTag, SqlExercise, SqlExerciseContent

sql_coll_1_ex_3: SqlExercise = SqlExercise(
    exerciseId=3,
    collectionId=1,
    toolId='sql',
    title='Emailadresse',
    authors=['bje40dc'],
    text='Welche Emailadresse hat Max Becker für die Arbeit?',
    topics=[],
    difficulty=1,
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
