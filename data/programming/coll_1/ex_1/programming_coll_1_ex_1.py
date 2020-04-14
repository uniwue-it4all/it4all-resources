from textwrap import dedent

from models.collection import Exercise, ExerciseState, ExerciseFile, SemanticVersion, SampleSolution, \
    load_text_from_file, base_res_path
from models.programming import ProgrammingExerciseContent, ProgrammingInput, ProgrammingUnitTestPart, \
    ProgrammingImplementationPart, ProgrammingUnitTestType, ProgrammingTestData, \
    ProgrammingSolution, ProgrammingExTag

unitTestPart: ProgrammingUnitTestPart = ProgrammingUnitTestPart(
    unitTestType=ProgrammingUnitTestType.Simplified,
    unitTestsDescription='TODO!',
    unitTestFiles=[],
    unitTestTestConfigs=[],
    simplifiedTestMainFile=ExerciseFile(
        name='test_main.py',
        fileType='python',
        editable=False,
        content=load_text_from_file(base_res_path / 'programming' / 'coll_1' / 'ex_1' / 'test_main.py'),
    ),
    testFileName='test_ggt.py',
    sampleSolFileNames=[]
)

implementationPart: ProgrammingImplementationPart = ProgrammingImplementationPart(
    base=dedent(
        """\
        def ggt(a: int, b: int) -> int:
            return 0
        """
    ),
    files=[
        ExerciseFile(
            name='ggt.py',
            fileType='python',
            editable=True,
            content=load_text_from_file(base_res_path / 'programming' / 'coll_1' / 'ex_1' / 'ggt_declaration.py')
        )
    ],
    implFileName='ggt.py',
    sampleSolFileNames=['ggt.py']
)

sampleSolution: SampleSolution[ProgrammingSolution] = SampleSolution(
    id=1,
    sample=ProgrammingSolution(
        files=[
            ExerciseFile(
                name='ggt.py',
                fileType='python',
                editable=True,
                content=load_text_from_file(base_res_path / 'programming' / 'coll_1' / 'ex_1' / 'ggt.py')
            )
        ],
        testData=[]
    )
)

programming_coll_1_ex_1: Exercise[ProgrammingExTag, ProgrammingExerciseContent] = Exercise(
    id=1,
    collectionId=1,
    toolId='programming',
    semanticVersion=SemanticVersion(major=1, minor=0, patch=0),
    title='Größter gemeinsamer Teiler',
    authors=['bje40dc'],
    text=load_text_from_file(base_res_path / 'programming' / 'coll_1' / 'ex_1' / 'text.html'),
    tags=[ProgrammingExTag.ForLoops, ProgrammingExTag.Conditions, ProgrammingExTag.Maths],
    state=ExerciseState.APPROVED,
    difficulty=2,
    content=ProgrammingExerciseContent(
        functionName='ggt',
        foldername='ggt',
        filename='ggt',
        inputTypes=[
            ProgrammingInput(id=1, inputName='a', inputType='INTEGER'),
            ProgrammingInput(id=2, inputName='b', inputType='INTEGER')
        ],
        outputType='INTEGER',
        unitTestPart=unitTestPart,
        implementationPart=implementationPart,
        sampleSolutions=[sampleSolution],
        sampleTestData=[
            ProgrammingTestData(id=1, input=[12, 4], output=4),
            ProgrammingTestData(id=2, input=[3, 7], output=1),
            ProgrammingTestData(id=3, input=[64, 46], output=2),
            ProgrammingTestData(id=4, input=[777, 111], output=111),
            ProgrammingTestData(id=5, input=[15, 25], output=5)
        ]
    )
)
