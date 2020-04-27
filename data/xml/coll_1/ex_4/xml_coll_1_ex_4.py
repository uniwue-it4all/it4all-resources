from pathlib import Path

from models.collection import SampleSolution, load_text_from_file, ex_resources_path
from models.xml import XmlSolution, XmlExercise, XmlExerciseContent

ex_res_path: Path = ex_resources_path('xml', 1, 4)

xml_coll_1_ex_4: XmlExercise = XmlExercise(
    exerciseId=4,
    collectionId=1,
    toolId='xml',
    title='Frühstück',
    authors=['bje40dc'],
    text='Erstellen Sie für dieses Xml-Dokument eine passende DTD.',
    topics=[],
    difficulty=1,
    content=XmlExerciseContent(
        rootNode='breakfast',
        grammarDescription=load_text_from_file(ex_res_path / 'grammarDescription.txt'),
        sampleSolutions=[
            SampleSolution(
                id=1,
                sample=XmlSolution(
                    grammar=load_text_from_file(ex_res_path / 'sol_1' / 'breakfast.dtd'),
                    document=load_text_from_file(ex_res_path / 'sol_1' / 'breakfast.xml')
                )
            )
        ]
    )
)
