from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional

from models.collection import SampleSolution


class SqlExerciseType(str, Enum):
    SELECT = 'SELECT'
    INSERT = 'INSERT'
    UPDATE = 'UPDATE'
    DELETE = 'DELETE'
    CREATE = 'CREATE'


class SqlExerciseTag(str, Enum):
    SQL_JOIN = 'SQL_JOIN'
    SQL_ORDER_BY = 'SQL_ORDER_BY'
    SQL_GROUP_BY = 'SQL_GROUP_BY'


@dataclass()
class SqlExerciseContent:
    exerciseType: SqlExerciseType
    sampleSolutions: List[SampleSolution[str]]
    tags: List[SqlExerciseTag] = field(default_factory=list)
    hint: Optional[str] = None
