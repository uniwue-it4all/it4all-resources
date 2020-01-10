from json import load as json_load
from logging import exception as log_exception
from pathlib import Path
from typing import Dict, Any, List, Optional

from models.basics import resource_base_dir

Lesson = Dict[str, Any]


def __update_lesson__(lesson: Lesson, tool_id: str):
    lesson_id: int = lesson['id']

    lesson['toolId'] = tool_id

    for content in lesson['content']:
        if content['_type'] == 'Text':
            file_path: Path = Path.cwd() / 'resources' / tool_id / 'lessons' / str(lesson_id) / content['contentFile']

            content.update({
                'lessonId': lesson_id,
                'toolId': tool_id,
                'content': file_path.read_text()
            })
        elif content['_type'] == 'Questions':
            qs_path: Path = Path.cwd() / 'resources' / tool_id / 'lessons' / str(lesson_id) / content['questionsFile']

            content.update({
                'lessonId': lesson_id,
                'toolId': tool_id,
                'questions': json_load(qs_path.open())
            })


def get_lesson_ids_for_tool(tool_id: str) -> List[int]:
    lessons_dir: Path = resource_base_dir / tool_id / 'lessons'
    return sorted([int(x.name) for x in lessons_dir.glob('*') if x.is_dir()])


def load_lessons(tool_id: str) -> List[Lesson]:
    lessons: List[Lesson] = []

    for lesson_id in get_lesson_ids_for_tool(tool_id):
        maybe_lesson: Optional[Lesson] = load_lesson(tool_id, lesson_id)

        if maybe_lesson is not None:
            lessons.append(maybe_lesson)

    return lessons


def load_lesson(tool_id: str, lesson_id: int, log_errors: bool = True) -> Optional[Lesson]:
    metadata_path = resource_base_dir / tool_id / 'lessons' / str(lesson_id) / 'lesson_metadata.json'

    if not metadata_path.exists():
        if log_errors:
            log_exception(f'Could not find metadata file {metadata_path}')
        return None

    try:
        loaded = json_load(metadata_path.open('r'))
        __update_lesson__(loaded, tool_id)
        return loaded
    except Exception as e:
        if log_errors:
            log_exception(e)
        return None
