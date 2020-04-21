from pathlib import Path

from models.collection import SampleSolution, load_text_from_file, ex_resources_path
from models.xml import XmlExercise, XmlSolution, XmlExerciseContent

ex_res_path: Path = ex_resources_path('xml', 1, 2)

xml_coll_1_ex_2: XmlExercise = XmlExercise(
    id=2,
    collectionId=1,
    toolId='xml',
    title='Vorlesung',
    authors=['bje40dc'],
    text='Erstellen Sie zu dieser DTD ein passendes Xml-Dokument.',
    topics=[],
    difficulty=2,
    content=XmlExerciseContent(
        rootNode='lecture',
        grammarDescription=load_text_from_file(ex_res_path / 'grammarDescription.txt'),
        sampleSolutions=[
            SampleSolution(
                id=1,
                sample=XmlSolution(
                    grammar=load_text_from_file(ex_res_path / 'sol_1' / 'lecture.dtd'),
                    document=load_text_from_file(ex_res_path / 'sol_1' / 'lecture.xml')
                )
            ),
            SampleSolution(
                id=2,
                sample=XmlSolution(
                    grammar=load_text_from_file(ex_res_path / 'sol_2' / 'lecture.dtd'),
                    document=load_text_from_file(ex_res_path / 'sol_2' / 'lecture.xml')
                )
            )
        ]
    )
)
