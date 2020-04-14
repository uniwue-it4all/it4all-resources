from typing import List

from data.uml.coll_1.uml_coll_1_ex_1 import uml_coll_1_ex_1
from data.uml.coll_1.uml_coll_1_ex_2 import uml_coll_1_ex_2
from models.collection import CollectionAndExes, Collection, Exercise
from models.uml import UmlExerciseContent, UmlExTag

uml_coll_1_exes: List[Exercise[UmlExTag, UmlExerciseContent]] = [
    uml_coll_1_ex_1,
    uml_coll_1_ex_2,
]

uml_collections_and_exes: List[CollectionAndExes[UmlExTag, UmlExerciseContent]] = [
    CollectionAndExes(
        Collection(
            id=1, toolId="uml", title="Uml Basics", authors=["bje40dc"],
            text="Aufgaben um die Grundlagen von UML-Klassendiagrammen zu erlernen.",
            shortName="uml_basics"
        ),
        {ex.id: ex for ex in uml_coll_1_exes}
    )
]
