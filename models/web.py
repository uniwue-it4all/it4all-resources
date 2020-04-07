from pathlib import Path
from typing import Dict, Any, TypedDict, Optional, List

from models.basics import update_exercise_files_field


def __check_attributes__(element_spec_json: Dict[str, Any]):
    if 'attributes' not in element_spec_json:
        element_spec_json['attributes'] = []


def update_site_spec(site_spec_json: Dict[str, Any]):
    for html_task_json in site_spec_json['htmlTasks']:
        __check_attributes__(html_task_json)

    for js_task_json in site_spec_json['jsTasks']:
        for pre_cond_json in js_task_json['preConditions']:
            __check_attributes__(pre_cond_json)

        for post_cond_json in js_task_json['postConditions']:
            __check_attributes__(post_cond_json)


def update_web_exercise_content(exercise_base_path: Path, content: Dict[str, Any]) -> Dict[str, Any]:
    update_exercise_files_field(exercise_base_path, content, 'files')

    update_site_spec(content['siteSpec'])

    for sample_json in content['sampleSolutions']:
        update_exercise_files_field(exercise_base_path, sample_json, 'sample')

    return content


class HtmlTask(TypedDict):
    id: int
    text: str
    xpath_query: str
    awaited_tag_name: str
    awaited_text_content: str


class JsTask(TypedDict):
    pass


class SiteSpec(TypedDict):
    file_name: str
    html_task: List[HtmlTask]
    js_tasks: List[JsTask]


class ExerciseFile(TypedDict):
    name: str
    resource_path: str
    file_type: str
    editable: bool


class WebSampleSolution(TypedDict):
    id: int
    sample: List[ExerciseFile]


class WebExerciseContent(TypedDict):
    html_text: Optional[str]
    js_text: Optional[str]
    files: List[ExerciseFile]
    site_spec: SiteSpec
    sample_solutions: List[WebSampleSolution]
