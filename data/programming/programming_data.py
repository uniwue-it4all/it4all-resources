from typing import List

from data.programming.coll_1.ex_1.programming_coll_1_ex_1 import programming_coll_1_ex_1
from data.programming.coll_1.ex_2.programming_coll_1_ex_2 import programming_coll_1_ex_2
from models.collection import CollectionAndExes, Collection
from models.programming import ProgrammingExercise

programming_coll_1_exes: List[ProgrammingExercise] = [
    programming_coll_1_ex_1, programming_coll_1_ex_2
]

programming_collections_and_exes: List[CollectionAndExes[ProgrammingExercise]] = [
    CollectionAndExes(
        Collection(
            id=1, toolId="programming", title="Zahlen", authors=["bje40dc"], text="TODO", shortName="numbers"
        ),
        {ex.id: ex for ex in programming_coll_1_exes}
    ),
    CollectionAndExes(
        Collection(
            id=2, toolId="programming", title="Strings", authors=["bje40dc"], text="TODO", shortName="strings"
        ),
        {ex.id: ex for ex in []}
    ),
    CollectionAndExes(
        Collection(
            id=3, toolId="programming", title="Bedingte Anweisungen", authors=["bje40dc"], text="TODO",
            shortName="conditions"
        ),
        {ex.id: ex for ex in []}
    ),
    CollectionAndExes(
        Collection(
            id=4, toolId="programming", title="Listen", authors=["bje40dc"], text="TODO", shortName="lists"
        ),
        {ex.id: ex for ex in []}
    ),
    CollectionAndExes(
        Collection(
            id=5, toolId="programming", title="Tupel und Dictionaries", authors=["bje40dc"], text="TODO",
            shortName="tuples_and_dicts"
        ),
        {ex.id: ex for ex in []}
    ),
    CollectionAndExes(
        Collection(
            id=6, toolId="programming", title="Funktionen", authors=["bje40dc"], text="TODO", shortName="functions"
        ),
        {ex.id: ex for ex in []}
    ),
    CollectionAndExes(
        Collection(
            id=7, toolId="programming", title="Klassen", authors=["bje40dc"], text="TODO", shortName="classes"
        ),
        {ex.id: ex for ex in []}
    ),
    CollectionAndExes(
        Collection(
            id=8, toolId='programming', title='Unit Testing', authors=['bje40dc'], text='TODO', shortName='unit_testing'
        ),
        {ex.id: ex for ex in []}
    )
]
