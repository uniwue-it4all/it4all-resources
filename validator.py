from models.basics import get_all_tool_ids
from models.collection import get_collection_ids_for_tool, load_collection
from models.exercise import load_exercise, get_exercise_ids_for_collection

for tool_id in get_all_tool_ids():
    print(f'Loading tool {tool_id}')

    for coll_id in get_collection_ids_for_tool(tool_id):
        # load all collections in tool
        print(f'Loading collection {coll_id}')
        load_collection(tool_id, coll_id)

        for ex_id in get_exercise_ids_for_collection(tool_id, coll_id):
            # load all exercises in collection
            print(f'Loading exercise {ex_id}')
            load_exercise(tool_id, coll_id, ex_id)
