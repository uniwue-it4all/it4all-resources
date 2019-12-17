from pathlib import Path
from typing import Dict, Any

from models.basics import resource_base_dir

Lesson = Dict[str, Any]


def get_lesson_ids_for_tool(tool_id: str):
    lessons_dir: Path = resource_base_dir / tool_id / 'lessons'
    return sorted([int(x.name) for x in lessons_dir.glob('*') if x.is_dir()])
