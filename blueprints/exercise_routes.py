from flask import Blueprint, url_for, request, jsonify

from models.exercise import load_exercise, load_exercises

exes_blueprint: Blueprint = Blueprint('exes', __name__)


@exes_blueprint.route('/')
def route_exercises(tool_id: str, coll_id: int):
    return jsonify({
        'parentUrl': request.host_url[:-1] + url_for('coll.route_collection', tool_id=tool_id, coll_id=coll_id),
        'exercises': load_exercises(tool_id, coll_id)
    })


@exes_blueprint.route('/<int:ex_id>')
def route_exercise(tool_id: str, coll_id: int, ex_id: int):
    return jsonify({
        'parentUrl': request.host_url[:-1] + url_for('coll.route_exercise_ids', tool_id=tool_id, coll_id=coll_id),
        'exercise': load_exercise(tool_id, coll_id, ex_id)
    })
