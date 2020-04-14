from typing import List

from models.collection import CollectionAndExes, Collection

programming_collections_and_exes: List[CollectionAndExes] = [
    CollectionAndExes(
        Collection(
            id=1, tool_id="programming", title="Zahlen", authors=["bje40dc"], text="TODO", short_name="numbers"
        ),
        {}
    ),
    CollectionAndExes(
        Collection(
            id=2, tool_id="programming", title="Strings", authors=["bje40dc"], text="TODO", short_name="strings"
        ),
        {}
    ),
    CollectionAndExes(
        Collection(
            id=3, tool_id="programming", title="Bedingte Anweisungen", authors=["bje40dc"], text="TODO",
            short_name="conditions"
        ),
        {}
    ),
    CollectionAndExes(
        Collection(
            id=4, tool_id="programming", title="Listen", authors=["bje40dc"], text="TODO", short_name="lists"
        ),
        {}
    ),
    CollectionAndExes(
        Collection(
            id=5, tool_id="programming", title="Tupel und Dictionaries", authors=["bje40dc"], text="TODO",
            short_name="tuples_and_dicts"
        ),
        {}
    ),
    CollectionAndExes(
        Collection(
            id=6, tool_id="programming", title="Funktionen", authors=["bje40dc"], text="TODO", short_name="functions"
        ),
        {}
    ),
    CollectionAndExes(
        Collection(
            id=7, tool_id="programming", title="Klassen", authors=["bje40dc"], text="TODO", short_name="classes"
        ),
        {}
    )
]
