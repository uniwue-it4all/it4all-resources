from textwrap import dedent

from models.collection import SampleSolution
from models.regex import RegexCorrectionType, RegexExtractionTestData, RegexExercise

regex_coll_2_ex_1: RegexExercise = RegexExercise(
    id=1,
    collectionId=2,
    toolId='regex',
    title='Heiße Preise',
    authors=['bje40dc'],
    text=dedent(
        """\
        Schreiben Sie einen regulären Ausdruck, der Preise aus Angeboten extrahiert.
        Diese sollen aus einer Ganz- oder Fließkommazahl mit maximal zwei Nachkommastellen bestehen.
        Es soll kein Symbol für eine Währungeinheit mitextrahiert werden."""
    ).replace('\n', ' '),
    topics=[],
    difficulty=3,
    maxPoints=2,
    correctionType=RegexCorrectionType.EXTRACTION,
    matchTestData=[],
    extractionTestData=[
        RegexExtractionTestData(
            id=1,
            base='Frische Äpfel= 2,99€/kg, Bananen= 3,49€/kg, Ananas 1,99€/Stück',
            toExtract=['2,99', '3,49', '1,99']
        ),
        RegexExtractionTestData(
            id=2,
            base='Reifenwechsel= 50€, Ölservice= 99€, Lichtcheck= 119,99€',
            toExtract=['50', '99', '119,99']
        )
    ],
    sampleSolutions=[
        SampleSolution(id=1, sample=r'\d+[,\d\d?]?')
    ]
)
