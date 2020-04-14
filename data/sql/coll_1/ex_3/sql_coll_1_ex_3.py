from textwrap import dedent

from models.collection import Exercise, ExerciseState, SemanticVersion, SampleSolution
from models.sql import SqlExerciseType, SqlExerciseContent, SqlExerciseTag

sql_coll_1_ex_3 = Exercise(
    id=3,
    collectionId=1,
    toolId='sql',
    semanticVersion=SemanticVersion(major=1, minor=0, patch=0),
    title='Emailadresse',
    authors=['bje40dc'],
    text='Welche Emailadresse hat Max Becker für die Arbeit?',
    tags=[],
    state=ExerciseState.APPROVED,
    difficulty=1,
    content=SqlExerciseContent(
        exerciseType=SqlExerciseType.SELECT,
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
        tags=[SqlExerciseTag.SQL_JOIN],
    )
)
