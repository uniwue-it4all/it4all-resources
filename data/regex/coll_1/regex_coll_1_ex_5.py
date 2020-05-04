from textwrap import dedent

from models.basics import SampleSolution
from models.regex import RegexMatchTestData, RegexCorrectionType, RegexExercise, RegexExerciseContent

content = RegexExerciseContent(
    maxPoints=4,
    correctionType=RegexCorrectionType.MATCHING,
    matchTestData=[
        RegexMatchTestData(id=1, data='james.bond@mi5.uk', isIncluded=True),
        RegexMatchTestData(id=2, data='jason_bourne@cia.gov', isIncluded=True),
        RegexMatchTestData(id=3, data='jack.bauer@24.com', isIncluded=True),
        RegexMatchTestData(id=4, data='xyz@localhost', isIncluded=False),
        RegexMatchTestData(id=5, data='@web.de', isIncluded=False),
        RegexMatchTestData(id=6, data='test.net', isIncluded=False)
    ],
    extractionTestData=[],
    sampleSolutions=[
        SampleSolution(
            id=1,
            sample=r'([a-z]|[A-Z]|[0-9]|_|-|\.)+@([a-z]|[A-Z]|[0-9]|_|-)+\.([a-z]|[A-Z]|[0-9]|_|-|\.)+'
        )
    ]
)

regex_coll_1_ex_5: RegexExercise = RegexExercise(
    exerciseId=5,
    collectionId=1,
    toolId='regex',
    title='E-Mail-Adressen',
    authors=['bje40dc'],
    text=dedent(
        """\
        Erstellen Sie einen regulären Ausdruck, der E-Mail-Adressen überprüfen kann.
        Eine Mailadresse besteht aus einem lokalen und einem Domänenteil, die durch ein @-Zeichen getrennt sind.
        Der Domänenteil wiederum besteht aus einem Hostnamen und einer Top-Level-Domain, die durch einen Punkt
        getrennt sind.
        Der Einfachkeit halber beschränken wir die Zeichen, die in einer Mailadresse vorkommen dürfen, auf alle
        Klein- und Großbuchstaben, alle Ziffern, Minus, Punkt und Unterstrich (_).
        Jeder Teil besteht aus mindestens einem dieser Zeichen."""
    ).replace('\n', ' '),
    difficulty=4,
    topicAbbreviations=[],
    content=content
)
