from typing import List

from data.web.coll_1.ex_1 import web_coll_1_ex_1
from data.web.coll_1.ex_2 import web_coll_1_ex_2
from models.collection import CollectionAndExes, Collection, Exercise
from models.web import WebExerciseContent

web_coll_1_exercises: List[Exercise[WebExerciseContent]] = [
    web_coll_1_ex_1,
    web_coll_1_ex_2
]

web_coll_2_exercises: List[Exercise[WebExerciseContent]] = [

]

web_collections_and_exes: List[CollectionAndExes[WebExerciseContent]] = [
    CollectionAndExes(
        Collection(
            id=1, tool_id="web", title="Html Elemente", authors=["bje40dc"], text="TODO", short_name="html_elements"
        ),
        {ex.id: ex for ex in web_coll_1_exercises}
    ),
    CollectionAndExes(
        Collection(
            id=2, tool_id="web", title="Js Basics", authors=["bje40dc"], text="TODO", short_name="js_basics"
        ),
        {ex.id: ex for ex in web_coll_2_exercises}
    )
]
