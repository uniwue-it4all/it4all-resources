from typing import List

from models.collection import Exercise, ExerciseState, SemanticVersion, SampleSolution, load_text_from_file, \
    base_res_path
from models.xml import XmlExerciseContent, XmlSolution

collection_id = 1
tool_id = 'xml'

coll_1_ex_1: Exercise[XmlExerciseContent] = Exercise(
    id=1,
    collection_id=collection_id,
    tool_id=tool_id,
    semantic_version=SemanticVersion(major=1, minor=0, patch=0),
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
        sample_solutions=[
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

coll_1_ex_2: Exercise[XmlExerciseContent] = Exercise(
    id=2,
    collection_id=collection_id,
    tool_id=tool_id,
    semantic_version=SemanticVersion(major=1, minor=0, patch=0),
    title='Vorlesung',
    authors=['bje40dc'],
    text='Erstellen Sie zu dieser DTD ein passendes Xml-Dokument.',
    tags=[],
    state=ExerciseState.APPROVED,
    difficulty=2,
    content=XmlExerciseContent(
        root_node='lecture',
        grammar_description=load_text_from_file(base_res_path / 'xml' / 'coll_1' / 'ex_2' / 'grammarDescription.txt'),
        sample_solutions=[
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

coll_1_ex_3: Exercise[XmlExerciseContent] = Exercise(
    id=3,
    collection_id=collection_id,
    tool_id=tool_id,
    semantic_version=SemanticVersion(major=1, minor=0, patch=0),
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

coll_1_ex_4: Exercise[XmlExerciseContent] = Exercise(
    id=4,
    collection_id=collection_id,
    tool_id=tool_id,
    semantic_version=SemanticVersion(major=1, minor=0, patch=0),
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

coll_1_ex_5: Exercise[XmlExerciseContent] = Exercise(
    id=5,
    collection_id=collection_id,
    tool_id=tool_id,
    semantic_version=SemanticVersion(major=1, minor=0, patch=0),
    title='Bibliothek',
    authors=['bje40dc'],
    text='Erstellen Sie für dieses Xml-Dokument eine passende DTD.',
    tags=[],
    state=ExerciseState.APPROVED,
    difficulty=2,
    content=XmlExerciseContent(
        root_node='bibliothek',
        grammar_description=load_text_from_file(base_res_path / 'xml' / 'coll_1' / 'ex_5' / 'grammarDescription.txt'),
        sample_solutions=[
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

coll_1_exercises: List[Exercise[XmlExerciseContent]] = [coll_1_ex_1, coll_1_ex_2, coll_1_ex_3, coll_1_ex_4, coll_1_ex_5]
