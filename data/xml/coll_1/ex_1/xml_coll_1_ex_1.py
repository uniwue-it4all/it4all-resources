from models.collection import Exercise, ExerciseState, SemanticVersion, SampleSolution, load_text_from_file, \
    base_res_path
from models.xml import XmlExerciseContent, XmlSolution, XmlExTag

xml_coll_1_ex_1: Exercise[XmlExTag, XmlExerciseContent] = Exercise(
    id=1,
    collectionId=1,
    toolId='xml',
    semanticVersion=SemanticVersion(major=1, minor=0, patch=0),
    title='Party',
    authors=['bje40dc'],
    text='Erstellen Sie zu dieser DTD ein passendes Xml-Dokument.',
    tags=[],
    state=ExerciseState.APPROVED,
    difficulty=1,
    content=XmlExerciseContent(
        root_node='party',
        grammar_description=load_text_from_file(
            base_res_path / 'xml' / 'coll_1' / 'ex_1' / 'grammarDescription.txt'
        ),
        sampleSolutions=[
            SampleSolution(
                id=1,
                sample=XmlSolution(
                    grammar=load_text_from_file(base_res_path / 'xml' / 'coll_1' / 'ex_1' / 'sol_1' / 'party.dtd'),
                    document=load_text_from_file(base_res_path / 'xml' / 'coll_1' / 'ex_1' / 'sol_1' / 'party.xml')
                )
            )
        ]
    )
)
