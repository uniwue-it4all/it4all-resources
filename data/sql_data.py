from typing import List

from models.collection import CollectionAndExes, Collection

sql_collections_and_exes: List[CollectionAndExes] = [
    CollectionAndExes(
        Collection(
            id=1, toolId="sql", title="Angestellte", authors=["bje40dc"],
            text="Dieses Szenario beschreibt die Datenbank einer kleinen Firma.", shortName="employee"
        ),
        {}
    ),
    CollectionAndExes(
        Collection(
            id=2, toolId="sql", title="Amazon", authors=["bje40dc"], text="", shortName="amazon"
        ),
        {}
    )
]
