from typing import List

from data.programming.coll_1.ex_1.programming_coll_1_ex_1 import programming_coll_1_ex_1
from data.programming.coll_1.ex_2.programming_coll_1_ex_2 import programming_coll_1_ex_2
from models.collection import CollectionAndExes, Collection
from models.programming import ProgrammingExercise

programming_coll_1_exes: List[ProgrammingExercise] = [
    programming_coll_1_ex_1, programming_coll_1_ex_2
]

programming_coll_2_exes: List[ProgrammingExercise] = []

programming_coll_3_exes: List[ProgrammingExercise] = []

programming_coll_4_exes: List[ProgrammingExercise] = []

programming_coll_5_exes: List[ProgrammingExercise] = []

programming_coll_6_exes: List[ProgrammingExercise] = []

programming_coll_7_exes: List[ProgrammingExercise] = []

programming_coll_8_exes: List[ProgrammingExercise] = []

programming_collections_and_exes: List[CollectionAndExes[ProgrammingExercise]] = [
    CollectionAndExes(
        Collection(collectionId=1, toolId="programming", title="Zahlen", authors=["bje40dc"], text="TODO"),
        {ex.exerciseId: ex for ex in programming_coll_1_exes}
    ),
    CollectionAndExes(
        Collection(collectionId=2, toolId="programming", title="Strings", authors=["bje40dc"], text="TODO"),
        {ex.exerciseId: ex for ex in programming_coll_2_exes}
    ),
    CollectionAndExes(
        Collection(collectionId=3, toolId="programming", title="Bedingungen", authors=["bje40dc"], text="TODO"),
        {ex.exerciseId: ex for ex in programming_coll_3_exes}
    ),
    CollectionAndExes(
        Collection(collectionId=4, toolId="programming", title="Listen", authors=["bje40dc"], text="TODO"),
        {ex.exerciseId: ex for ex in programming_coll_4_exes}
    ),
    CollectionAndExes(
        Collection(collectionId=5, toolId="programming", title="Tupel und Dicts", authors=["bje40dc"], text="TODO"),
        {ex.exerciseId: ex for ex in programming_coll_5_exes}
    ),
    CollectionAndExes(
        Collection(collectionId=6, toolId="programming", title="Funktionen", authors=["bje40dc"], text="TODO"),
        {ex.exerciseId: ex for ex in programming_coll_6_exes}
    ),
    CollectionAndExes(
        Collection(collectionId=7, toolId="programming", title="Klassen", authors=["bje40dc"], text="TODO"),
        {ex.exerciseId: ex for ex in programming_coll_7_exes}
    ),
    CollectionAndExes(
        Collection(collectionId=8, toolId='programming', title='Unit Testing', authors=['bje40dc'], text='TODO'),
        {ex.exerciseId: ex for ex in programming_coll_8_exes}
    )
]
