from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Any, List

from models.basics import read_long_text_from_file
from models.collection import SampleSolution


def update_xml_exercise_content(base_path: Path, content: Dict[str, Any]):
    content['grammarDescription'] = read_long_text_from_file(base_path, content['grammarDescription'])
    pass


@dataclass()
class XmlSolution:
    document: str
    grammar: str


@dataclass()
class XmlExerciseContent:
    root_node: str
    grammar_description: str
    sample_solutions: List[SampleSolution[XmlSolution]]
