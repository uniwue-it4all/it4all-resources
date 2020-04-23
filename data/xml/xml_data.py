from typing import List

from data.xml.coll_1.ex_1.xml_coll_1_ex_1 import xml_coll_1_ex_1
from data.xml.coll_1.ex_2.xml_coll_1_ex_2 import xml_coll_1_ex_2
from data.xml.coll_1.ex_3.xml_coll_1_ex_3 import xml_coll_1_ex_3
from data.xml.coll_1.ex_4.xml_coll_1_ex_4 import xml_coll_1_ex_4
from data.xml.coll_1.ex_5.xml_coll_1_ex_5 import xml_coll_1_ex_5
from models.collection import CollectionAndExes, Collection
from models.xml import XmlExercise

xml_coll_1_exercises: List[XmlExercise] = [
    xml_coll_1_ex_1, xml_coll_1_ex_2, xml_coll_1_ex_3,
    xml_coll_1_ex_4, xml_coll_1_ex_5
]

xml_collections_and_exes: List[CollectionAndExes[XmlExercise]] = [
    CollectionAndExes(
        Collection(id=1, toolId="xml", title="Xml Basics", authors=["bje40dc"], text="TODO"),
        {ex.id: ex for ex in xml_coll_1_exercises}
    )
]
