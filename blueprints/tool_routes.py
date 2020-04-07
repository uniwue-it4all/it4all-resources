from typing import Dict, List, TypedDict, Any

from animal_case import animalify
from flask import Blueprint, url_for, jsonify

from data.programming_data import programming_collections
from data.web_data import web_collections
from models.collection import Collection
from models.lesson import get_lesson_ids_for_tool

tool_blueprint: Blueprint = Blueprint('tool', __name__)


class ToolValues(TypedDict):
    collections: List[Collection]
    lessons: List[Any]


all_tools: Dict[str, ToolValues] = {
    'programming': {
        'collections': programming_collections,
        'lessons': []
    },
    'regex': {
        'collections': [],
        'lessons': []
    },
    'rose': {
        'collections': [],
        'lessons': []
    },
    'sql': {
        'collections': [],
        'lessons': []
    },
    'uml': {
        'collections': [],
        'lessons': []
    },
    'web': {
        'collections': web_collections,
        'lessons': []
    },
    'xml': {
        'collections': [],
        'lessons': []
    },
}


@tool_blueprint.route('/')
def route_tools():
    return jsonify(
        animalify({
            'tools': [
                {
                    'id': tool_id,
                    'tool_url': url_for('tool.route_tool', tool_id=tool_id, _external=True)
                } for tool_id in all_tools.keys()
            ]
        })
    )


@tool_blueprint.route('/<string:tool_id>')
def route_tool(tool_id: str):
    tool_values = all_tools[tool_id]

    collections = tool_values['collections']
    lessons = tool_values['lessons']

    return jsonify(
        animalify({
            'parent_url': url_for('tool.route_tools', _external=True),
            'tool_id': tool_id,
            'collections': {
                'count': len([co for co in collections]),
                'collection_ids': [
                    {
                        'id': collection['id'],
                        'url': url_for(
                            'coll.route_collection', tool_id=tool_id, coll_id=collection['id'], _external=True
                        )
                    } for collection in collections
                ],
                'collections_url': url_for('tool.route_collections', tool_id=tool_id, _external=True)
            },
            'lessons': {
                'count': len([le for le in lessons]),
                'lesson_ids': [
                    {
                        'id': lesson['id'],
                        'url': url_for('lesson.route_lesson', tool_id=tool_id, lesson_id=lesson['id'], _external=True)
                    } for lesson in lessons],
                'lessons_url': url_for('lessons.route_lessons', tool_id=tool_id, _external=True)
            }
        })
    )


# collection routes

@tool_blueprint.route('/<string:tool_id>/collectionIds')
def route_collection_ids(tool_id: str):
    tool_values = all_tools[tool_id]

    return jsonify(
        animalify({
            'parentUrl': url_for('tool.route_tool', tool_id=tool_id, _external=True),
            'collections': [
                {
                    'id': collection['id'],
                    'collectionUrl': url_for(
                        'coll.route_collection', tool_id=tool_id, coll_id=collection['id'], _external=True
                    )
                } for collection in tool_values['collections']
            ]
        })
    )


@tool_blueprint.route('/<string:tool_id>/collections')
def route_collections(tool_id: str):
    return jsonify(
        animalify({
            'parentUrl': url_for('tool.route_tool', tool_id=tool_id, _external=True),
            'collections': all_tools[tool_id]['collections']
        })
    )


# lesson routes

@tool_blueprint.route('/<string:tool_id>/lessonIds')
def route_lesson_ids(tool_id: str):
    return jsonify(
        animalify({
            'parentUrl': url_for('tool.route_tool', tool_id=tool_id, _external=True),
            'lessons': [
                {
                    'id': lesson_id,
                    'lessonUrl': url_for('lessons.route_lesson', tool_id=tool_id, lesson_id=lesson_id, _external=True)
                } for lesson_id in get_lesson_ids_for_tool(tool_id)
            ]
        })
    )
