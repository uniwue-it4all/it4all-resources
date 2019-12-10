from sys import stderr
from typing import Dict, Union

from models.basics import get_all_tool_ids
from models.collection import get_collection_ids_for_tool, load_collection
from models.exercise import load_exercise, get_exercise_ids_for_collection

for tool_id in get_all_tool_ids():
    for coll_id in get_collection_ids_for_tool(tool_id):
        # load all collections in tool
        if not load_collection(tool_id, coll_id):
            print(f'Could not load collection {tool_id}-{coll_id}', file=stderr)

        for ex_id in get_exercise_ids_for_collection(tool_id, coll_id):
            # load all exercises in collection
            maybe_ex: Union[str, Dict] = load_exercise(tool_id, coll_id, ex_id, False)
            if isinstance(maybe_ex, str):
                print(f'Could not load exercise {tool_id}-{coll_id}-{ex_id}:', file=stderr)
                print(maybe_ex)
