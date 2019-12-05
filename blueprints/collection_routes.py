from typing import Optional, List

from flask import Blueprint, jsonify, redirect, url_for, request

from models.collection import get_collection_ids_for_tool, load_collections, ExerciseCollection, load_collection

coll_blueprint: Blueprint = Blueprint('coll_blueprint', __name__)


@coll_blueprint.route('/collectionIds')
def route_collection_ids(tool_id: str):
    return jsonify({
        'parentUrl': request.host_url[:-1] + url_for('tool_blueprint.route_tool', tool_id=tool_id),
        'collections': [
            {
                'id': coll_id,
                'collectionUrl': request.host_url[:-1] + url_for(
                    'coll_blueprint.route_collection', tool_id=tool_id, coll_id=coll_id)
            } for coll_id in get_collection_ids_for_tool(tool_id)
        ]
    })


@coll_blueprint.route('/collections')
def route_collections(tool_id: str):
    collections: List[ExerciseCollection] = load_collections(tool_id)

    return jsonify({
        'parentUrl': request.host_url[:-1] + url_for('tool_blueprint.route_tool', tool_id=tool_id),
        'collections': [c.to_json_dict() for c in collections]
    })


@coll_blueprint.route('/collections/<int:coll_id>')
def route_collection(tool_id: str, coll_id: int):
    parent_url: str = url_for('coll_blueprint.route_collections', tool_id=tool_id)

    collection_metadata: Optional[ExerciseCollection] = load_collection(tool_id, coll_id)

    if not collection_metadata:
        return redirect(parent_url)

    return jsonify({
        'parentUrl': request.host_url[:-1] + parent_url,
        'metaData': collection_metadata.to_json_dict(),
        'exerciseIdsUrl': request.host_url[:-1] + url_for(
            'exes_blueprint.route_exercise_ids', tool_id=tool_id, coll_id=coll_id),
        'exercisesUrl': request.host_url[:-1] + url_for(
            'exes_blueprint.route_exercises', tool_id=tool_id, coll_id=coll_id)
    })
