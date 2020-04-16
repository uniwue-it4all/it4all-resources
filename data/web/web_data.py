from typing import List

from data.web.coll_1.ex_1.web_coll_1_ex_1 import web_coll_1_ex_1
from data.web.coll_1.ex_2.web_coll_1_ex_2 import web_coll_1_ex_2
from data.web.coll_1.ex_3.web_coll_1_ex_3 import web_coll_1_ex_3
from data.web.coll_1.ex_4.web_coll_1_ex_4 import web_coll_1_ex_4
from data.web.coll_1.ex_5.web_coll_1_ex_5 import web_coll_1_ex_5
from data.web.coll_2.ex_1.web_coll_2_ex_1 import web_coll_2_ex_1
from data.web.coll_2.ex_2.web_coll_2_ex_2 import web_coll_2_ex_2
from data.web.coll_2.ex_3.web_coll_2_ex_3 import web_coll_2_ex_3
from models.collection import CollectionAndExes, Collection
from models.web import WebExercise

web_coll_1_exercises: List[WebExercise] = [
    web_coll_1_ex_1, web_coll_1_ex_2, web_coll_1_ex_3,
    web_coll_1_ex_4, web_coll_1_ex_5
]

web_coll_2_exercises: List[WebExercise] = [
    web_coll_2_ex_1, web_coll_2_ex_2, web_coll_2_ex_3
]

web_collections_and_exes: List[CollectionAndExes[WebExercise]] = [
    CollectionAndExes(
        Collection(
            id=1, toolId="web", title="Html Elemente", authors=["bje40dc"], text="TODO", shortName="html_elements"
        ),
        {ex.id: ex for ex in web_coll_1_exercises}
    ),
    CollectionAndExes(
        Collection(
            id=2, toolId="web", title="Js Basics", authors=["bje40dc"], text="TODO", shortName="js_basics"
        ),
        {ex.id: ex for ex in web_coll_2_exercises}
    )
]
