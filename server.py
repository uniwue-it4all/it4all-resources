from typing import List, Dict, Optional

from flask import Flask, jsonify, url_for

from model import get_tools, get_collection_ids_for_tool, get_collection_metadata, get_exercise_ids_for_collection

app = Flask(__name__)

base_url: str = 'http://localhost:5000'


@app.route('/')
def route_index():
    tool_names: List[Dict[str, str]] = [
        {
            'tool_name': tool_name,
            'tool_url': base_url + url_for('route_collections', tool_id=tool_name)
        } for tool_name in get_tools()
    ]

    return jsonify(tool_names)


@app.route('/<string:tool_id>/collections')
def route_collections(tool_id: str):
    collection_ids_for_tool: List[int] = get_collection_ids_for_tool(tool_id)

    collection_metadata: List[Optional[dict]] = [
        get_collection_metadata(tool_id, collection_id) for collection_id in collection_ids_for_tool
    ]

    for metadata in collection_metadata:
        if metadata is not None:
            relative_url: str = url_for('route_exercises', tool_id=tool_id, collection_id=metadata['id'])
            metadata['collection_url'] = base_url + relative_url

    return jsonify(collection_metadata)


@app.route('/<string:tool_id>/<int:collection_id>/exercises')
def route_exercises(tool_id: str, collection_id: int):
    exercise_ids_for_collection: List[int] = get_exercise_ids_for_collection(tool_id, collection_id)

    return jsonify(exercise_ids_for_collection)


if __name__ == "__main__":
    app.debug = True
    app.run()
