from typing import List

from data.regex.coll_1.regex_coll_1_ex_1 import regex_coll_1_ex_1
from data.regex.coll_1.regex_coll_1_ex_2 import regex_coll_1_ex_2
from data.regex.coll_1.regex_coll_1_ex_3 import regex_coll_1_ex_3
from data.regex.coll_1.regex_coll_1_ex_4 import regex_coll_1_ex_4
from data.regex.coll_1.regex_coll_1_ex_5 import regex_coll_1_ex_5
from data.regex.coll_2.regex_coll_2_ex_1 import regex_coll_2_ex_1
from data.regex.coll_2.regex_coll_2_ex_2 import regex_coll_2_ex_2
from models.collection import CollectionAndExes, Collection
from models.regex import RegexExercise

regex_coll_1_exes: List[RegexExercise] = [
    regex_coll_1_ex_1, regex_coll_1_ex_2, regex_coll_1_ex_3,
    regex_coll_1_ex_4, regex_coll_1_ex_5
]

regex_coll_2_exes: List[RegexExercise] = [
    regex_coll_2_ex_1, regex_coll_2_ex_2
]

regex_collections_and_exes: List[CollectionAndExes[RegexExercise]] = [
    CollectionAndExes(
        Collection(collectionId=1, toolId="regex", title="Zahlen und Fakten", authors=["bje40dc"], text="TODO"),
        {ex.exerciseId: ex for ex in regex_coll_1_exes}
    ),
    CollectionAndExes(
        Collection(collectionId=2, toolId="regex", title="Informationsextraktion", authors=["bje40dc"], text="TODO"),
        {ex.exerciseId: ex for ex in regex_coll_2_exes}
    )
]
