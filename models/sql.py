from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional

from models.basics import SampleSolution, Exercise


class SqlExerciseType(str, Enum):
    SELECT = 'SELECT'
    INSERT = 'INSERT'
    UPDATE = 'UPDATE'
    DELETE = 'DELETE'
    CREATE = 'CREATE'


class SqlExTag(str, Enum):
    SQL_JOIN = 'SQL_JOIN'
    SQL_ORDER_BY = 'SQL_ORDER_BY'
    SQL_GROUP_BY = 'SQL_GROUP_BY'
    SQL_FUNCTION = 'SQL_FUNCTION'
    SQL_ALIAS = 'SQL_ALIAS'
    SQL_DOUBLE_JOIN = 'SQL_DOUBLE_JOIN'
    SQL_LIMIT = 'SQL_LIMIT'
    SQL_SELECT = 'SQL_SELECT'
    SQL_UPDATE = 'SQL_UPDATE'
    SQL_DELETE = 'SQL_DELETE'
    SQL_INSERT = 'SQL_INSERT'


@dataclass()
class SqlExerciseContent:
    exerciseType: SqlExerciseType
    schemaName: str
    sampleSolutions: List[SampleSolution[str]]
    tags: List[SqlExTag] = field(default_factory=list)
    hint: Optional[str] = None


@dataclass()
class SqlExercise(Exercise):
    content: SqlExerciseContent
