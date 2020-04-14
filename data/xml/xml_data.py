from typing import List

from data.xml.xml_coll_1_exes import xml_coll_1_exercises
from models.collection import CollectionAndExes, Collection

xml_collections_and_exes: List[CollectionAndExes] = [
    CollectionAndExes(
        Collection(
            id=1, toolId="xml", title="Xml Basics", authors=["bje40dc"], text="TODO", shortName="xml_basics"
        ),
        {ex.id: ex for ex in xml_coll_1_exercises}
    )
]
