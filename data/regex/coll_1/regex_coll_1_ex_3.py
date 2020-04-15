from textwrap import dedent

from models.collection import Exercise, ExerciseState, SemanticVersion, SampleSolution
from models.regex import RegexMatchTestData, RegexExerciseContent, RegexCorrectionType, RegexExTag

regex_coll_1_ex_3: Exercise[RegexExTag, RegexExerciseContent] = Exercise(
    id=3,
    collectionId=1,
    toolId='regex',
    semanticVersion=SemanticVersion(major=0, minor=0, patch=1),
    title='Komlexe Datumsangaben',
    authors=['bje40dc'],
    text=dedent(
        """\
        Schreiben Sie einen regulären Ausdruck, der eine komplexere Version von Datumsangaben überprüfen kann.
        Dabei sollen der Tag und der Monat jeweils aus ein oder zwei und die Jahresangabe aus zwei bis vier Ziffern bestehen.
        Als Trennzeichen soll jeweils ein Punkt verwendet werden.
        Eine Validierung auf kalendarische Korrektheit ist nicht erforderlich.
        Führende Nullen sind erlaubt."""
    ).replace('\n', ' '),
    tags=[],
    state=ExerciseState.APPROVED,
    difficulty=3,
    content=RegexExerciseContent(
        maxPoints=3,
        correctionType=RegexCorrectionType.MATCHING,
        matchTestData=[
            RegexMatchTestData(id=1, data='12.01.1999', isIncluded=True),
            RegexMatchTestData(id=2, data='99.17.3006', isIncluded=True),
            RegexMatchTestData(id=3, data='33.11.1931', isIncluded=True),
            RegexMatchTestData(id=4, data='1.1.1999', isIncluded=True),
            RegexMatchTestData(id=5, data='01.01.0700', isIncluded=True),
            RegexMatchTestData(id=6, data='01.01.700', isIncluded=True),
            RegexMatchTestData(id=7, data='3.12.2011', isIncluded=True),
            RegexMatchTestData(id=8, data='29.3.2018', isIncluded=True),
            RegexMatchTestData(id=9, data='1.1.1', isIncluded=False),
            RegexMatchTestData(id=10, data='12.10', isIncluded=False),
            RegexMatchTestData(id=11, data='11.2.', isIncluded=False),
            RegexMatchTestData(id=12, data='12-01-1999', isIncluded=False)
        ],
        extractionTestData=[],
        sampleSolutions=[
            SampleSolution(id=1, sample='\d\d?\.\d\d?\.\d\d\d?\d?'),
            SampleSolution(id=2, sample='\d{1,2}\.\d{1,2}\.\d{2,4}'),
            SampleSolution(id=3, sample='[0-9]{1,2}\.[0-9]{1,2}\.[0-9]{2,4}')
        ]
    )
)