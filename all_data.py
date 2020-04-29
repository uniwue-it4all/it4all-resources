from typing import Dict

from data.programming.programming_data import programming_collections_and_exes
from data.regex.regex_data import regex_collections_and_exes
from data.sql.sql_data import sql_collections_and_exes
from data.uml.uml_data import uml_collections_and_exes
from data.web.web_data import web_collections_and_exes
from data.xml.xml_data import xml_collections_and_exes
from models.collection import ToolValues

all_tools: Dict[str, ToolValues] = {
    'programming': ToolValues(
        {pc.collection.collectionId: pc for pc in programming_collections_and_exes},
        {}
    ),
    'regex': ToolValues(
        {rc.collection.collectionId: rc for rc in regex_collections_and_exes},
        {}
    ),
    'rose': ToolValues({}, {}),
    'sql': ToolValues(
        {sc.collection.collectionId: sc for sc in sql_collections_and_exes},
        {}
    ),
    'uml': ToolValues(
        {uc.collection.collectionId: uc for uc in uml_collections_and_exes},
        {}
    ),
    'web': ToolValues(
        {wc.collection.collectionId: wc for wc in web_collections_and_exes},
        {}
    ),
    'xml': ToolValues(
        {xc.collection.collectionId: xc for xc in xml_collections_and_exes},
        {}
    ),
}
