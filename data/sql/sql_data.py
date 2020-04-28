from typing import List

from data.sql.sql_coll_1_exes import sql_coll_1_exes
from data.sql.sql_coll_2_exes import sql_coll_2_exes
from models.collection import CollectionAndExes, Collection
from models.sql import SqlExercise

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
