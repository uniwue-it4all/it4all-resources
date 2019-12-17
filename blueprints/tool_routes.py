from typing import Dict, Any

from flask import Blueprint, request, url_for, jsonify

from models.basics import get_all_tool_ids
from models.collection import get_collection_ids_for_tool
from models.lesson import get_lesson_ids_for_tool

tool_blueprint: Blueprint = Blueprint('tool', __name__)


@tool_blueprint.route('/')
def route_tools():
    return jsonify({
        'tools': [
            {
                'id': tool_id,
                'toolUrl': request.host_url[:-1] + url_for('tool.route_tool', tool_id=tool_id)
            } for tool_id in get_all_tool_ids()
        ]
    })


@tool_blueprint.route('/<string:tool_id>')
def route_tool(tool_id: str):
    host_url: str = request.host_url[:-1]

    data: Dict[str, Any] = {
        'parentUrl': host_url + url_for('tool.route_tools'),
        'tool_id': tool_id,
        'collections': 'No Collections found!',
        'lessons': 'No Lessons found!'
    }

    if len(get_collection_ids_for_tool(tool_id)) > 0:
        data['collections'] = {
            'collectionIdsUrl': host_url + url_for('tool.route_collection_ids', tool_id=tool_id),
            'collectionsUrl': host_url + url_for('coll.route_collections', tool_id=tool_id),
        }

    if len(get_lesson_ids_for_tool(tool_id)) > 0:
        data['lessons'] = {
            'lessonIdsUrl': host_url + url_for('tool.route_lesson_ids', tool_id=tool_id),
            'lessonsUrl': host_url + url_for('lessons.route_lessons', tool_id=tool_id)
        }

    return jsonify(data)


@tool_blueprint.route('/<string:tool_id>/lessonIds')
def route_lesson_ids(tool_id: str):
    host_url: str = request.host_url[:-1]

    return jsonify({
        'parentUrl': host_url + url_for('tool.route_tool', tool_id=tool_id),
        'lessons': [
            {
                'id': lesson_id,
                'lessonUrl': host_url + url_for('lessons.route_lesson', tool_id=tool_id, lesson_id=lesson_id)
            } for lesson_id in get_lesson_ids_for_tool(tool_id)
        ]
    })


@tool_blueprint.route('/<string:tool_id>/collectionIds')
def route_collection_ids(tool_id: str):
    host_url: str = request.host_url[:-1]

    return jsonify({
        'parentUrl': host_url + url_for('tool.route_tool', tool_id=tool_id),
        'collections': [
            {
                'id': coll_id,
                'collectionUrl': host_url + url_for('coll.route_collection', tool_id=tool_id, coll_id=coll_id)
            } for coll_id in get_collection_ids_for_tool(tool_id)
        ]
    })
