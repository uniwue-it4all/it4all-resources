from models.collection import Exercise, ExerciseState, SemanticVersion, SampleSolution, load_text_from_file, \
    base_res_path
from models.xml import XmlExerciseContent, XmlSolution

xml_coll_1_ex_4: Exercise[XmlExerciseContent] = Exercise(
    id=4,
    collectionId=1,
    toolId='xml',
    semanticVersion=SemanticVersion(major=1, minor=0, patch=0),
    title='Frühstück',
    authors=['bje40dc'],
    text='Erstellen Sie für dieses Xml-Dokument eine passende DTD.',
    tags=[],
    state=ExerciseState.APPROVED,
    difficulty=1,
    content=XmlExerciseContent(
        root_node='breakfast',
        grammar_description=load_text_from_file(base_res_path / 'xml' / 'coll_1' / 'ex_4' / 'grammarDescription.txt'),
        sample_solutions=[
            SampleSolution(
                id=1,
                sample=XmlSolution(
                    grammar=load_text_from_file(base_res_path / 'xml' / 'coll_1' / 'ex_4' / 'sol_1' / 'breakfast.dtd'),
                    document=load_text_from_file(base_res_path / 'xml' / 'coll_1' / 'ex_4' / 'sol_1' / 'breakfast.xml')
                )
            )
        ]
    )
)
