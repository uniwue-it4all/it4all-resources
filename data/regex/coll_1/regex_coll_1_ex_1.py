from textwrap import dedent

from models.collection import Exercise, SemanticVersion, ExerciseState, SampleSolution
from models.regex import RegexExerciseContent, RegexCorrectionType, RegexMatchTestData, RegexExTag

regex_coll_1_ex_1: Exercise[RegexExTag, RegexExerciseContent] = Exercise(
    id=1,
    collectionId=1,
    toolId='regex',
    semanticVersion=SemanticVersion(major=0, minor=0, patch=1),
    title='Postleitzahlen',
    authors=['bje40dc'],
    text=dedent(
        """\
        Schreiben Sie einen regulären Ausdruck, der (deutsche) Postleitzahlen überprüfen kann.
        Diese bestehen aus 5 Ziffern."""
    ).replace('\n', ' '),
    tags=[],
    state=ExerciseState.APPROVED,
    difficulty=1,
    content=RegexExerciseContent(
        maxPoints=1,
        correctionType=RegexCorrectionType.MATCHING,
        matchTestData=[
            RegexMatchTestData(id=1, data='97070', isIncluded=True),
            RegexMatchTestData(id=2, data='90210', isIncluded=True),
            RegexMatchTestData(id=3, data='10115', isIncluded=True),
            RegexMatchTestData(id=4, data='65432', isIncluded=True),
            RegexMatchTestData(id=5, data='01234', isIncluded=True),
            RegexMatchTestData(id=6, data='8911', isIncluded=False),
            RegexMatchTestData(id=7, data='654321', isIncluded=False)
        ],
        extractionTestData=[],
        sampleSolutions=[
            SampleSolution(id=1, sample=r'\d{5}'),
            SampleSolution(id=2, sample=r'[0-9]{5}'),
            SampleSolution(id=3, sample=r'\d\d\d\d\d')
        ]
    )
)
