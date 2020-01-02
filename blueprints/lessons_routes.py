from flask import Blueprint, jsonify, url_for, request

from models.lesson import load_lesson, load_lessons

lessons_blueprint: Blueprint = Blueprint('lessons', __name__)


@lessons_blueprint.route('/')
def route_lessons(tool_id: str):
    return jsonify({
        'parentUrl': request.host_url[:-1] + url_for('tool.route_tool', tool_id=tool_id),
        'lessons': load_lessons(tool_id)
    })


@lessons_blueprint.route('/<int:lesson_id>')
def route_lesson(tool_id: str, lesson_id: int):
    host_url: str = request.host_url[:-1]

    return jsonify({
        'parentUrl': host_url + url_for('lessons.route_lessons', tool_id=tool_id),
        'metaData': load_lesson(tool_id, lesson_id)
    })
