from textwrap import dedent

from models.collection import ExerciseState, Exercise, SampleSolution, SemanticVersion
from models.regex import RegexExerciseContent, RegexCorrectionType, RegexMatchTestData

regex_coll_1_ex_4: Exercise[RegexExerciseContent] = Exercise(
    id=4,
    collectionId=1,
    toolId='regex',
    semanticVersion=SemanticVersion(major=0, minor=0, patch=1),
    title='Semantische Versionierung',
    authors=['bje40dc'],
    text=dedent(
        """\
        Schreiben Sie einen regulären Ausruck, der semantische Versionsnummern überprüfen kann.
        Diese bestehen aus einer Haupt-, einer Neben-, einer Revisions- und einer optionalen Buildnummer, die jeweils
        mit einem Punkt beziehungsweise im Fall der Revisions- und Buildnummer mit einem Minus getrennt werden.
        Jede der Nummern kann mehrstellig sein und führende Nullen besitzen."""
    ).replace('\n', ' '),
    tags=[],
    state=ExerciseState.APPROVED,
    difficulty=3,
    content=RegexExerciseContent(
        maxPoints=3,
        correctionType=RegexCorrectionType.MATCHING,
        matchTestData=[
            RegexMatchTestData(id=1, data='2.3.5-0041', isIncluded=True),
            RegexMatchTestData(id=2, data='0.0.1', isIncluded=True),
            RegexMatchTestData(id=3, data='1.3.3-7', isIncluded=True),
            RegexMatchTestData(id=4, data='1.12.2-21', isIncluded=True),
            RegexMatchTestData(id=5, data='2.05.7-11', isIncluded=True),
            RegexMatchTestData(id=6, data='1.0', isIncluded=False),
            RegexMatchTestData(id=7, data='1..10', isIncluded=False),
            RegexMatchTestData(id=8, data='1..10', isIncluded=False),
            RegexMatchTestData(id=9, data='1.0-3', isIncluded=False)
        ],
        extractionTestData=[],
        sampleSolutions=[
            SampleSolution(id=1, sample=r'\d+\.\d+\.\d+(-\d+)?'),
            SampleSolution(id=2, sample=r'[0-9]+\.[0-9]+\.[0-9]+(-[0-9]+)?')
        ]
    )
)
