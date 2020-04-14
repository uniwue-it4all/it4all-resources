from models.collection import Exercise, ExerciseState, SemanticVersion, SampleSolution, load_text_from_file, \
    base_res_path
from models.xml import XmlExerciseContent, XmlSolution, XmlExTag

xml_coll_1_ex_2: Exercise[XmlExTag, XmlExerciseContent] = Exercise(
    id=2,
    collectionId=1,
    toolId='xml',
    semanticVersion=SemanticVersion(major=1, minor=0, patch=0),
    title='Vorlesung',
    authors=['bje40dc'],
    text='Erstellen Sie zu dieser DTD ein passendes Xml-Dokument.',
    tags=[],
    state=ExerciseState.APPROVED,
    difficulty=2,
    content=XmlExerciseContent(
        root_node='lecture',
        grammar_description=load_text_from_file(base_res_path / 'xml' / 'coll_1' / 'ex_2' / 'grammarDescription.txt'),
        sampleSolutions=[
            SampleSolution(
                id=1,
                sample=XmlSolution(
                    grammar=load_text_from_file(base_res_path / 'xml' / 'coll_1' / 'ex_2' / 'sol_1' / 'lecture.dtd'),
                    document=load_text_from_file(base_res_path / 'xml' / 'coll_1' / 'ex_2' / 'sol_1' / 'lecture.xml')
                )
            ),
            SampleSolution(
                id=2,
                sample=XmlSolution(
                    grammar=load_text_from_file(base_res_path / 'xml' / 'coll_1' / 'ex_2' / 'sol_2' / 'lecture.dtd'),
                    document=load_text_from_file(base_res_path / 'xml' / 'coll_1' / 'ex_2' / 'sol_2' / 'lecture.xml')
                )
            )
        ]
    )
)
