from typing import List

from models.collection import CollectionAndExes, Collection
from models.rose import RoseExercise
from data.rose.coll_1.ex_1.rose_coll_1_ex_1 import rose_coll_1_ex_1
from data.rose.coll_1.ex_2.rose_coll_1_ex_2 import rose_coll_1_ex_2

rose_coll_1_exes: List[RoseExercise] = [
    rose_coll_1_ex_1, rose_coll_1_ex_2
]

rose_collections_and_exes: List[CollectionAndExes[RoseExercise]] = [
    CollectionAndExes(
        Collection(
            collectionId=1, toolId="rose", title="Rose Basics", authors=["bje40dc"],
            text="Einfache Aufgaben um den Umgang mit diesem Tool zu lernen",
        ),
        {ex.exerciseId: ex for ex in rose_coll_1_exes}
    )
]
