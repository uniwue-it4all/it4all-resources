from pathlib import Path

from models.collection import SampleSolution, load_text_from_file, ex_resources_path
from models.xml import XmlExercise, XmlSolution

ex_res_path: Path = ex_resources_path('xml', 1, 1)

xml_coll_1_ex_1: XmlExercise = XmlExercise(
    id=1,
    collectionId=1,
    toolId='xml',
    title='Party',
    authors=['bje40dc'],
    text='Erstellen Sie zu dieser DTD ein passendes Xml-Dokument.',
    topics=[],
    difficulty=1,
    rootNode='party',
    grammarDescription=load_text_from_file(ex_res_path / 'grammarDescription.txt'),
    sampleSolutions=[
        SampleSolution(
            id=1,
            sample=XmlSolution(
                grammar=load_text_from_file(ex_res_path / 'sol_1' / 'party.dtd'),
                document=load_text_from_file(ex_res_path / 'sol_1' / 'party.xml')
            )
        )
    ]
)
