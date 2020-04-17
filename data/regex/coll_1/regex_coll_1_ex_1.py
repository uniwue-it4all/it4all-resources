from textwrap import dedent

from models.collection import SampleSolution
from models.regex import RegexCorrectionType, RegexMatchTestData, RegexExercise, RegexExerciseContent

regex_coll_1_ex_1: RegexExercise = RegexExercise(
    id=1,
    collectionId=1,
    toolId='regex',
    title='Postleitzahlen',
    authors=['bje40dc'],
    text=dedent(
        """\
        Schreiben Sie einen regulären Ausdruck, der (deutsche) Postleitzahlen überprüfen kann.
        Diese bestehen aus 5 Ziffern."""
    ).replace('\n', ' '),
    topics=[],
    difficulty=1,
    sampleSolutions=[
        SampleSolution(id=1, sample=r'\d{5}'),
        SampleSolution(id=2, sample=r'[0-9]{5}'),
        SampleSolution(id=3, sample=r'\d\d\d\d\d')
    ],
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
    )
)
