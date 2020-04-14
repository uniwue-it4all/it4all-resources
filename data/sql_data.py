from typing import List

from models.collection import CollectionAndExes, Collection

sql_collections_and_exes: List[CollectionAndExes] = [
    CollectionAndExes(
        Collection(
            id=1, tool_id="sql", title="Angestellte", authors=["bje40dc"],
            text="Dieses Szenario beschreibt die Datenbank einer kleinen Firma.", short_name="employee"
        ),
        {}
    ),
    CollectionAndExes(
        Collection(
            id=2, tool_id="sql", title="Amazon", authors=["bje40dc"], text="", short_name="amazon"
        ),
        {}
    )
]
