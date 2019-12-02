from typing import List, Optional, Dict, Any

from flask import Flask, jsonify, url_for, redirect

from model import get_tool_ids, get_collection_ids_for_tool, get_collection_metadata, get_exercise_ids_for_collection, \
    tool_exists, collection_exists, get_exercise_metadata
from models.exercise import Exercise

app = Flask(__name__)

base_url: str = 'http://localhost:5000'


@app.route('/')
def route_index():
    return redirect(url_for('route_tools'))


@app.route('/tools')
def route_tools():
    tools: List[Dict[str, str]] = [
        {
            'id': tool_id,
            'toolUrl': base_url + url_for('route_tool', tool_id=tool_id)
        } for tool_id in get_tool_ids()
    ]

    return jsonify({'tools': tools})


@app.route('/tools/<string:tool_id>')
def route_tool(tool_id: str):
    parent_url: str = url_for('route_tools')

    if not tool_exists(tool_id):
        return redirect(parent_url)

    return jsonify({
        'parentUrl': base_url + parent_url,
        'tool_id': tool_id,
        'lessonsUrl': '',
        'collectionsUrl': base_url + url_for('route_collections', tool_id=tool_id)
    })


@app.route('/tools/<string:tool_id>/collections')
def route_collections(tool_id: str):
    collection_ids = [
        {
            'id': coll_id,
            'collectionUrl': base_url + url_for('route_collection', tool_id=tool_id, coll_id=coll_id)
        } for coll_id in get_collection_ids_for_tool(tool_id)
    ]

    return jsonify({
        'parentUrl': base_url + url_for('route_tool', tool_id=tool_id),
        'collections': collection_ids
    })


@app.route('/tools/<string:tool_id>/collections/<int:coll_id>')
def route_collection(tool_id: str, coll_id: int):
    parent_url: str = url_for('route_collections', tool_id=tool_id)

    collection_metadata: Optional[Dict] = get_collection_metadata(tool_id, coll_id)

    if not collection_metadata:
        return redirect(parent_url)

    return jsonify({
        'parentUrl': base_url + parent_url,
        'metaData': collection_metadata,
        'exercisesUrl': base_url + url_for('route_exercises', tool_id=tool_id, coll_id=coll_id)
    })


@app.route('/tools/<string:tool_id>/collections/<int:coll_id>/exercises')
def route_exercises(tool_id: str, coll_id: int):
    parent_url: str = url_for('route_collection', tool_id=tool_id, coll_id=coll_id)

    if not collection_exists(tool_id, coll_id):
        return redirect(parent_url)

    exercise_ids_for_collection: List[Dict[str, Any]] = [
        {
            'id': ex_id,
            'exerciseUrl': base_url + url_for('route_exercise', tool_id=tool_id, coll_id=coll_id, ex_id=ex_id)
        } for ex_id in get_exercise_ids_for_collection(tool_id, coll_id)
    ]

    return jsonify({
        'parentUrl': base_url + parent_url,
        'exercises': exercise_ids_for_collection
    })


@app.route('/tools/<string:tool_id>/collections/<int:coll_id>/exercises/<int:ex_id>')
def route_exercise(tool_id: str, coll_id: int, ex_id: int):
    parent_url: str = url_for('route_exercises', tool_id=tool_id, coll_id=coll_id)

    exercise_metadata: Optional[Exercise] = get_exercise_metadata(tool_id, coll_id, ex_id)

    # FIXME: load LongText column!

    if not exercise_metadata:
        return redirect(parent_url)

    return jsonify({
        'parentUrl': base_url + parent_url,
        'metaData': exercise_metadata.to_json()
    })


if __name__ == "__main__":
    app.debug = True
    app.config["JSON_SORT_KEYS"] = False
    app.run(host='0.0.0.0')
