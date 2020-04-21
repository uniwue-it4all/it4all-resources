from pathlib import Path

from models.collection import SampleSolution, load_text_from_file, ex_resources_path
from models.xml import XmlSolution, XmlExercise, XmlExerciseContent

ex_res_path: Path = ex_resources_path('xml', 1, 3)

xml_coll_1_ex_3: XmlExercise = XmlExercise(
    id=3,
    collectionId=1,
    toolId='xml',
    title='Krankenhaus',
    authors=['bje40dc'],
    text='Erstellen Sie zu dieser DTD ein passendes Xml-Dokument.',
    topics=[],
    difficulty=1,
    content=XmlExerciseContent(
        rootNode='praxis',
        grammarDescription=load_text_from_file(ex_res_path / 'grammarDescription.txt'),
        sampleSolutions=[
            SampleSolution(
                id=1,
                sample=XmlSolution(
                    grammar=load_text_from_file(ex_res_path / 'sol_1' / 'praxis.dtd'),
                    document=load_text_from_file(ex_res_path / 'sol_1' / 'praxis.xml')
                )
            )
        ]
    )
)
