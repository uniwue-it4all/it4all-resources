from pathlib import Path
from textwrap import dedent

from models.collection import SampleSolution, Exercise, ex_resources_path, SemanticVersion, load_text_from_file, \
    ExerciseState, ExerciseFile
from models.programming import ProgrammingExerciseContent, ProgrammingUnitTestPart, ProgrammingUnitTestType, \
    ProgrammingUnitTestTestConfig, ProgrammingImplementationPart, ProgrammingExTag, ProgrammingInput, \
    ProgrammingSolution

ex_res_path: Path = ex_resources_path('programming', 1, 2)

unit_test_part: ProgrammingUnitTestPart = ProgrammingUnitTestPart(
    unitTestType=ProgrammingUnitTestType.Normal,
    unitTestsDescription=dedent(
        """\
        Schreiben Sie Unittests für die Funktion <code>factorial(n= int) -> int</code>.
        Diese soll die Fakultät der Zahl <code>n</code> berechnen.
        Der Funktionsparameter <code>n</code> soll größer als 0 sein."""
    ).replace('\n', ' '),
    unitTestFiles=[
        ExerciseFile(
            name='factorial.py',
            fileType='python',
            editable=False,
            content=load_text_from_file(ex_res_path / 'factorial_declaration.py'),
        ),
        ExerciseFile(
            name='test_factorial.py',
            fileType='python',
            editable=True,
            content=load_text_from_file(ex_res_path / 'test_factorial_declaration.py'),
        )
    ],
    unitTestTestConfigs=[
        ProgrammingUnitTestTestConfig(
            id=0,
            shouldFail=False,
            description='Diese Implementierung ist korrekt und sollte alle Tests bestehen.',
            file=ExerciseFile(
                name='factorial_0.py',
                fileType='python',
                editable=False,
                content=load_text_from_file(ex_res_path / 'unit_test_sols' / 'factorial_0.py')
            )
        ),
        ProgrammingUnitTestTestConfig(
            id=1,
            shouldFail=True,
            description="""Falls das Funktionsargument 'n' keine Ganzzahl ist, soll eine Exception geworfen werden.""",
            file=ExerciseFile(
                name='factorial_1.py',
                fileType='python',
                editable=False,
                content=load_text_from_file(ex_res_path / 'unit_test_sols' / 'factorial_1.py'),
            )
        ),
        ProgrammingUnitTestTestConfig(
            id=2,
            shouldFail=True,
            description='Falls das Funktionsargument kleiner oder gleich 0 ist, soll eine Exception geworfen werden.',
            file=ExerciseFile(
                name='factorial_2.py',
                fileType='python',
                editable=False,
                content=load_text_from_file(ex_res_path / 'unit_test_sols' / 'factorial_2.py'),
            )
        ),
        ProgrammingUnitTestTestConfig(
            id=3,
            shouldFail=True,
            description='Die Funktion soll das richtige Resultat zurückliefern.',
            file=ExerciseFile(
                name='factorial_3.py',
                fileType='python',
                editable=False,
                content=load_text_from_file(ex_res_path / 'unit_test_sols' / 'factorial_3.py'),
            )
        )
    ],
    testFileName='test_factorial.py',
    sampleSolFileNames=['test_factorial.py']
)

implementation_part: ProgrammingImplementationPart = ProgrammingImplementationPart(
    base=dedent(
        """\
        def factorial(n: int) -> int:
            pass
        """
    ),
    files=[
        ExerciseFile(
            name='test_factorial.py',
            fileType='python',
            editable=False,
            content=load_text_from_file(ex_res_path / 'test_factorial.py'),
        ),
        ExerciseFile(
            name='factorial.py',
            fileType='python',
            editable=True,
            content=load_text_from_file(ex_res_path / 'factorial_declaration.py'),
        )
    ],
    implFileName='factorial.py',
    sampleSolFileNames=['factorial.py']
)

programming_coll_1_ex_2: Exercise[ProgrammingExTag, ProgrammingExerciseContent] = Exercise(
    id=2,
    collectionId=1,
    toolId='programming',
    semanticVersion=SemanticVersion(major=1, minor=0, patch=0),
    title='Fakultät',
    authors=['bje40dc'],
    text=load_text_from_file(ex_res_path / 'text.html'),
    tags=[ProgrammingExTag.Exceptions, ProgrammingExTag.Maths, ProgrammingExTag.ForLoops],
    state=ExerciseState.APPROVED,
    difficulty=1,
    content=ProgrammingExerciseContent(
        functionName='factorial',
        foldername='factorial',
        filename='factorial',
        inputTypes=[
            ProgrammingInput(id=1, inputName='n', inputType='INTEGER')
        ],
        outputType='INTEGER',
        unitTestPart=unit_test_part,
        implementationPart=implementation_part,
        sampleTestData=[],
        sampleSolutions=[
            SampleSolution(
                id=1,
                sample=ProgrammingSolution(
                    files=[
                        ExerciseFile(
                            name='test_factorial.py',
                            fileType='python',
                            editable=False,
                            content=load_text_from_file(ex_res_path / 'test_factorial.py'),
                        ),
                        ExerciseFile(
                            name='factorial.py',
                            fileType='python',
                            editable=False,
                            content=load_text_from_file(ex_res_path / 'factorial.py'),
                        )
                    ],
                    testData=[]
                )

            )
        ]
    )
)
