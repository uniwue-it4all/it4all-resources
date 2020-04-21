from pathlib import Path

from models.collection import SampleSolution, load_text_from_file, base_res_path, ex_resources_path
from models.xml import XmlSolution, XmlExercise, XmlExerciseContent

ex_res_path: Path = ex_resources_path('xml', 1, 5)

xml_coll_1_ex_5: XmlExercise = XmlExercise(
    id=5,
    collectionId=1,
    toolId='xml',
    title='Bibliothek',
    authors=['bje40dc'],
    text='Erstellen Sie für dieses Xml-Dokument eine passende DTD.',
    topics=[],
    difficulty=2,
    content=XmlExerciseContent(
        rootNode='bibliothek',
        grammarDescription=load_text_from_file(base_res_path / 'xml' / 'coll_1' / 'ex_5' / 'grammarDescription.txt'),
        sampleSolutions=[
            SampleSolution(
                id=1,
                sample=XmlSolution(
                    grammar=load_text_from_file(ex_res_path / 'sol_1' / 'library.dtd'),
                    document=load_text_from_file(ex_res_path / 'sol_1' / 'library.xml'),
                )
            ),
            SampleSolution(
                id=2,
                sample=XmlSolution(
                    grammar=load_text_from_file(ex_res_path / 'sol_2' / 'library.dtd'),
                    document=load_text_from_file(ex_res_path / 'sol_2' / 'library.xml')
                )
            )
        ]
    )
)
