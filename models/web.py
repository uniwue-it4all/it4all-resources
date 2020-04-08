from dataclasses import dataclass, field
from typing import Optional, List

from models.collection import SampleSolution, ExerciseFile


@dataclass()
class HtmlAttribute:
    key: str
    value: str


@dataclass()
class HtmlTask:
    id: int
    text: str
    xpath_query: str
    awaited_tag_name: str
    awaited_text_content: Optional[str] = None
    attributes: List[HtmlAttribute] = field(default_factory=list)


@dataclass()
class JsTask:
    pass


@dataclass()
class SiteSpec:
    file_name: str
    html_tasks: List[HtmlTask]
    js_tasks: List[JsTask]


@dataclass()
class WebSolution:
    files: List[ExerciseFile]


@dataclass
class WebExerciseContent:
    files: List[ExerciseFile]
    site_spec: SiteSpec
    sample_solutions: List[SampleSolution[WebSolution]]
    html_text: Optional[str] = None
    js_text: Optional[str] = None
