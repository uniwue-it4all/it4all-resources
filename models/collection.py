from enum import Enum
from typing import List, TypedDict


class ToolState(Enum):
    PRE_ALPHA = 'PRE_ALPHA'
    ALPHA = 'ALPHA'
    BETA = 'BETA'
    LIVE = 'LIVE'


class Collection(TypedDict):
    id: int
    tool_id: str
    title: str
    authors: List[str]
    text: str
    short_name: str


class Exercise(TypedDict):
    id: int
