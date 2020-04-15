from dataclasses import dataclass, field
from enum import Enum
from typing import Optional, List

from models.collection import ExerciseFile, ExerciseContent


class JsActionType(str, Enum):
    Click = 'Click'
    FillOut = 'FillOut'


class WebExTag(str, Enum):
    pass


@dataclass()
class HtmlAttribute:
    key: str
    value: str


@dataclass()
class HtmlTask:
    id: int
    text: str
    xpathQuery: str
    awaitedTagName: str
    awaitedTextContent: Optional[str] = None
    attributes: List[HtmlAttribute] = field(default_factory=list)


@dataclass()
class JsAction:
    xpathQuery: str
    actionType: JsActionType
    keysToSend: Optional[str] = None


@dataclass()
class JsCondition:
    id: int
    xpathQuery: str
    awaitedTagName: str
    awaitedTextContent: Optional[str]
    attributes: List[HtmlAttribute] = field(default_factory=list)


@dataclass()
class JsTask:
    id: int
    text: str
    preConditions: List[JsCondition]
    action: JsAction
    postConditions: List[JsCondition]


@dataclass()
class SiteSpec:
    fileName: str
    htmlTasks: List[HtmlTask]
    jsTasks: List[JsTask]


@dataclass()
class WebSolution:
    files: List[ExerciseFile]


@dataclass
class WebExerciseContent(ExerciseContent[WebSolution]):
    files: List[ExerciseFile]
    siteSpec: SiteSpec
    htmlText: Optional[str] = None
    jsText: Optional[str] = None
