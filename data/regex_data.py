from typing import List

from models.collection import CollectionAndExes, Collection

regex_collections_and_exes: List[CollectionAndExes] = [
    CollectionAndExes(
        Collection(
            id=1, tool_id="regex", title="Zahlen und Fakten", authors=["bje40dc"], text="TODO",
            short_name="numbers_facts"
        ),
        []
    ),
    CollectionAndExes(
        Collection(
            id=2, tool_id="regex", title="Informationsextraktion", authors=["bje40dc"], text="TODO",
            short_name="extraction"
        ),
        []
    )
]
