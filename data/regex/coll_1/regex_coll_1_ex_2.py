from textwrap import dedent

from models.basics import SampleSolution
from models.regex import RegexCorrectionType, RegexMatchTestData, RegexExercise, RegexExerciseContent

content: RegexExerciseContent = RegexExerciseContent(
    maxPoints=2,
    correctionType=RegexCorrectionType.MATCHING,
    matchTestData=[
        RegexMatchTestData(id=1, data='12.01.1999', isIncluded=True),
        RegexMatchTestData(id=2, data='99.17.3006', isIncluded=True),
        RegexMatchTestData(id=3, data='33.11.1931', isIncluded=True),
        RegexMatchTestData(id=4, data='01.01.0700', isIncluded=True),
        RegexMatchTestData(id=5, data='1.1.1999', isIncluded=False),
        RegexMatchTestData(id=6, data='01.01.700', isIncluded=False),
        RegexMatchTestData(id=7, data='3.12.2011', isIncluded=False),
        RegexMatchTestData(id=8, data='29.3.2018', isIncluded=False),
        RegexMatchTestData(id=9, data='12-01-1999', isIncluded=False),
        RegexMatchTestData(id=10, data='1.1.1', isIncluded=False),
        RegexMatchTestData(id=11, data='12.10', isIncluded=False),
        RegexMatchTestData(id=12, data='11.2.', isIncluded=False),
    ],
    extractionTestData=[],
    sampleSolutions=[
        SampleSolution(id=1, sample=r'\d\d\.\d\d\.\d\d\d\d'),
        SampleSolution(id=2, sample=r'\d{2}\.\d{2}\.\d{4}'),
        SampleSolution(id=3, sample=r'[0-9]{2}\.[0-9]{2}\.[0-9]{4}')
    ],
)

regex_coll_1_ex_2: RegexExercise = RegexExercise(
    exerciseId=2,
    collectionId=1,
    toolId='regex',
    title='Einfache Datumsangaben',
    authors=['bje40dc'],
    text=dedent(
        """\
        Schreiben Sie einen regulären Ausdruck, der eine einfache Version von Datumsangaben findet.
        Dabei sollen der Tag und der Monat jeweils aus zwei und die Jahresangabe aus vier Zahlen bestehen.
        Als Trennzeichen soll jeweils ein Punkt verwendet werden.
        Eine Validierung auf kalendarische Korrektheit (zum Beispiel, dass der 30.02.2019 oder der 99.17.3005 nicht
        existieren) ist nicht erforderlich.
        Außerdem sind führende Nullen erlaubt."""
    ).replace('\n', ' '),
    difficulty=2,
    topicAbbreviations=[],
    content=content
)
