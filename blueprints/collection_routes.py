from flask import Blueprint, jsonify, url_for, request

from models.collection import load_collections, load_collection
from models.exercise import get_exercise_ids_for_collection

coll_blueprint: Blueprint = Blueprint('coll', __name__)


@coll_blueprint.route('/')
def route_collections(tool_id: str):
    return jsonify({
        'parentUrl': request.host_url[:-1] + url_for('tool.route_tool', tool_id=tool_id),
        'collections': load_collections(tool_id)
    })


@coll_blueprint.route('/<int:coll_id>')
def route_collection(tool_id: str, coll_id: int):
    host_url: str = request.host_url[:-1]

    return jsonify({
        'parentUrl': host_url + url_for('coll.route_collections', tool_id=tool_id),
        'metaData': load_collection(tool_id, coll_id),
        'exerciseIdsUrl': host_url + url_for('coll.route_exercise_ids', tool_id=tool_id, coll_id=coll_id),
        'exercisesUrl': host_url + url_for('exes.route_exercises', tool_id=tool_id, coll_id=coll_id)
    })


@coll_blueprint.route('/<int:coll_id>/exerciseIds')
def route_exercise_ids(tool_id: str, coll_id: int):
    host_url: str = request.host_url[:-1]

    return jsonify({
        'parentUrl': host_url + url_for('coll.route_collection', tool_id=tool_id, coll_id=coll_id),
        'exercises': [
            {
                'id': ex_id,
                'exerciseUrl': host_url + url_for('exes.route_exercise', tool_id=tool_id, coll_id=coll_id, ex_id=ex_id)
            } for ex_id in get_exercise_ids_for_collection(tool_id, coll_id)
        ]
    })
