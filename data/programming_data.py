from typing import List

from models.collection import CollectionAndExes, Collection

programming_collections_and_exes: List[CollectionAndExes] = [
    CollectionAndExes(
        Collection(
            id=1, toolId="programming", title="Zahlen", authors=["bje40dc"], text="TODO", shortName="numbers"
        ),
        {}
    ),
    CollectionAndExes(
        Collection(
            id=2, toolId="programming", title="Strings", authors=["bje40dc"], text="TODO", shortName="strings"
        ),
        {}
    ),
    CollectionAndExes(
        Collection(
            id=3, toolId="programming", title="Bedingte Anweisungen", authors=["bje40dc"], text="TODO",
            shortName="conditions"
        ),
        {}
    ),
    CollectionAndExes(
        Collection(
            id=4, toolId="programming", title="Listen", authors=["bje40dc"], text="TODO", shortName="lists"
        ),
        {}
    ),
    CollectionAndExes(
        Collection(
            id=5, toolId="programming", title="Tupel und Dictionaries", authors=["bje40dc"], text="TODO",
            shortName="tuples_and_dicts"
        ),
        {}
    ),
    CollectionAndExes(
        Collection(
            id=6, toolId="programming", title="Funktionen", authors=["bje40dc"], text="TODO", shortName="functions"
        ),
        {}
    ),
    CollectionAndExes(
        Collection(
            id=7, toolId="programming", title="Klassen", authors=["bje40dc"], text="TODO", shortName="classes"
        ),
        {}
    )
]
