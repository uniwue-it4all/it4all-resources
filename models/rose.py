from dataclasses import dataclass
from typing import List, Dict

from models.collection import Exercise, SampleSolution


@dataclass()
class RoseExerciseContent:
    fieldWidth: int
    fieldHeight: int
    isMultiplayer: bool
    inputTypes: List[Dict]
    sampleSolutions: List[SampleSolution[str]]


@dataclass()
class RoseExercise(Exercise):
    content: RoseExerciseContent
