from models.collection import Exercise, ExerciseState, SemanticVersion, SampleSolution, load_text_from_file, \
    base_res_path
from models.xml import XmlExerciseContent, XmlSolution

xml_coll_1_ex_3: Exercise[XmlExerciseContent] = Exercise(
    id=3,
    collectionId=1,
    toolId='xml',
    semanticVersion=SemanticVersion(major=1, minor=0, patch=0),
    title='Krankenhaus',
    authors=['bje40dc'],
    text='Erstellen Sie zu dieser DTD ein passendes Xml-Dokument.',
    tags=[],
    state=ExerciseState.APPROVED,
    difficulty=1,
    content=XmlExerciseContent(
        root_node='praxis',
        grammar_description=load_text_from_file(base_res_path / 'xml' / 'coll_1' / 'ex_3' / 'grammarDescription.txt'),
        sample_solutions=[
            SampleSolution(
                id=1,
                sample=XmlSolution(
                    grammar=load_text_from_file(base_res_path / 'xml' / 'coll_1' / 'ex_3' / 'sol_1' / 'praxis.dtd'),
                    document=load_text_from_file(base_res_path / 'xml' / 'coll_1' / 'ex_3' / 'sol_1' / 'praxis.xml')
                )
            )
        ]
    )
)
