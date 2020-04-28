from typing import List

from data.sql.sql_coll_1_exes import sql_coll_1_exes
from data.sql.sql_coll_2_exes_01_to_10 import sql_coll_2_exes_01_to_10
from data.sql.sql_coll_2_exes_11_to_20 import sql_coll_2_exes_11_to_20
from data.sql.sql_coll_2_exes_21_to_30 import sql_coll_2_exes_21_to_30
from data.sql.sql_coll_2_exes_31_to_40 import sql_coll_2_exes_31_to_40
from data.sql.sql_coll_2_exes_41_to_50 import sql_coll_2_exes_41_to_50
from models.collection import CollectionAndExes, Collection
from models.sql import SqlExercise

sql_coll_2_exes: List[SqlExercise] = [
    *sql_coll_2_exes_01_to_10,
    *sql_coll_2_exes_11_to_20,
    *sql_coll_2_exes_21_to_30,
    *sql_coll_2_exes_31_to_40,
    *sql_coll_2_exes_41_to_50
]

sql_collections_and_exes: List[CollectionAndExes[SqlExercise]] = [
    CollectionAndExes(
        Collection(
            collectionId=1, toolId="sql", title="Angestellte", authors=["bje40dc"],
            text="Dieses Szenario beschreibt die Datenbank einer kleinen Firma."
        ),
        {ex.exerciseId: ex for ex in sql_coll_1_exes}
    ),
    CollectionAndExes(
        Collection(collectionId=2, toolId="sql", title="Amazon", authors=["bje40dc"], text=""),
        {ex.exerciseId: ex for ex in sql_coll_2_exes}
    )
]
