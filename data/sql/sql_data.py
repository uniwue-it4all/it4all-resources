from typing import List

from data.sql.coll_1.ex_1.sql_coll_1_ex_1 import sql_coll_1_ex_1
from data.sql.coll_1.ex_2.sql_coll_1_ex_2 import sql_coll_1_ex_2
from data.sql.coll_1.ex_3.sql_coll_1_ex_3 import sql_coll_1_ex_3
from data.sql.coll_1.ex_4.sql_coll_1_ex_4 import sql_coll_1_ex_4
from data.sql.coll_1.ex_5.sql_coll_1_ex_5 import sql_coll_1_ex_5
from data.sql.coll_1.ex_6.sql_coll_1_ex_6 import sql_coll_1_ex_6
from data.sql.coll_1.ex_7.sql_coll_1_ex_7 import sql_coll_1_ex_7
from data.sql.coll_1.ex_8.sql_coll_1_ex_8 import sql_coll_1_ex_8
from data.sql.coll_1.ex_9.sql_coll_1_ex_9 import sql_coll_1_ex_9
from models.collection import CollectionAndExes, Collection, Exercise
from models.sql import SqlExerciseContent

sql_coll_1_exes: List[Exercise[SqlExerciseContent]] = [
    sql_coll_1_ex_1, sql_coll_1_ex_2, sql_coll_1_ex_3,
    sql_coll_1_ex_4, sql_coll_1_ex_5, sql_coll_1_ex_6,
    sql_coll_1_ex_7, sql_coll_1_ex_8, sql_coll_1_ex_9
]

sql_coll_2_exes: List[Exercise[SqlExerciseContent]] = [

]

sql_collections_and_exes: List[CollectionAndExes] = [
    CollectionAndExes(
        Collection(
            id=1, toolId="sql", title="Angestellte", authors=["bje40dc"],
            text="Dieses Szenario beschreibt die Datenbank einer kleinen Firma.", shortName="employee"
        ),
        {ex.id: ex for ex in sql_coll_1_exes}
    ),
    CollectionAndExes(
        Collection(
            id=2, toolId="sql", title="Amazon", authors=["bje40dc"], text="", shortName="amazon"
        ),
        {ex.id: ex for ex in sql_coll_2_exes}
    )
]
