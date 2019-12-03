from pathlib import Path
from typing import List, Optional

from flask import Blueprint, url_for, request, redirect, jsonify

from models.basics import resource_base_dir
from models.exercise import Exercise, get_exercise_ids_for_collection, load_exercise, load_exercises

exes_blueprint: Blueprint = Blueprint('exes_blueprint', __name__)


def collection_exists(tool_id: str, coll_id: int) -> bool:
    metadata_file: Path = resource_base_dir / tool_id / str(coll_id) / 'collection_metadata.json'
    return metadata_file.exists()


@exes_blueprint.route('/exerciseIds')
def route_exercise_ids(tool_id: str, coll_id: int):
    parent_url: str = url_for('coll_blueprint.route_collection', tool_id=tool_id, coll_id=coll_id)

    if not collection_exists(tool_id, coll_id):
        return redirect(parent_url)

    exercise_ids: List[int] = get_exercise_ids_for_collection(tool_id, coll_id)

    return jsonify({
        'parentUrl': request.host_url[:-1] + parent_url,
        'exercises': [
            {
                'id': ex_id,
                'exerciseUrl': request.host_url[:-1] + url_for(
                    'exes_blueprint.route_exercise', tool_id=tool_id, coll_id=coll_id, ex_id=ex_id)
            } for ex_id in exercise_ids
        ]
    })


@exes_blueprint.route('/exercises')
def route_exercises(tool_id: str, coll_id: int):
    exercises_metadata: List[Exercise] = load_exercises(tool_id, coll_id)

    return jsonify({
        'parentUrl': request.host_url[:-1] + url_for(
            'coll_blueprint.route_collection', tool_id=tool_id, coll_id=coll_id),
        'exercises': exercises_metadata
    })


@exes_blueprint.route('/exercises/<int:ex_id>')
def route_exercise(tool_id: str, coll_id: int, ex_id: int):
    parent_url: str = url_for('exes_blueprint.route_exercise_ids', tool_id=tool_id, coll_id=coll_id)

    exercise_metadata: Optional[Exercise] = load_exercise(tool_id, coll_id, ex_id)

    # FIXME: load LongText column!

    if not exercise_metadata:
        return redirect(parent_url)

    return jsonify({
        'parentUrl': request.host_url[:-1] + parent_url,
        'metaData': exercise_metadata
    })
