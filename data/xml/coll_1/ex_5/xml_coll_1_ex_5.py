from models.collection import Exercise, ExerciseState, SemanticVersion, SampleSolution, load_text_from_file, \
    base_res_path
from models.xml import XmlExerciseContent, XmlSolution, XmlExTag

xml_coll_1_ex_5: Exercise[XmlExTag, XmlExerciseContent] = Exercise(
    id=5,
    collectionId=1,
    toolId='xml',
    semanticVersion=SemanticVersion(major=1, minor=0, patch=0),
    title='Bibliothek',
    authors=['bje40dc'],
    text='Erstellen Sie für dieses Xml-Dokument eine passende DTD.',
    tags=[],
    state=ExerciseState.APPROVED,
    difficulty=2,
    content=XmlExerciseContent(
        root_node='bibliothek',
        grammar_description=load_text_from_file(base_res_path / 'xml' / 'coll_1' / 'ex_5' / 'grammarDescription.txt'),
        sampleSolutions=[
            SampleSolution(
                id=1,
                sample=XmlSolution(
                    grammar=load_text_from_file(base_res_path / 'xml' / 'coll_1' / 'ex_5' / 'sol_1' / 'library.dtd'),
                    document=load_text_from_file(base_res_path / 'xml' / 'coll_1' / 'ex_5' / 'sol_1' / 'library.xml'),
                )
            ),
            SampleSolution(
                id=2,
                sample=XmlSolution(
                    grammar=load_text_from_file(base_res_path / 'xml' / 'coll_1' / 'ex_5' / 'sol_2' / 'library.dtd'),
                    document=load_text_from_file(base_res_path / 'xml' / 'coll_1' / 'ex_5' / 'sol_2' / 'library.xml')
                )
            )
        ]
    )
)
