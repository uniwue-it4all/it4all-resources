from pathlib import Path
from typing import Dict, Any
from models.basics import read_long_text_from_file


def update_xml_exercise_content(base_path: Path, content: Dict[str, Any]):
    content['grammarDescription'] = read_long_text_from_file(base_path, content['grammarDescription'])
    pass
