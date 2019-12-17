from flask import Blueprint

lessons_blueprint: Blueprint = Blueprint('lessons', __name__)


@lessons_blueprint.route('/')
def route_lessons(tool_id: str):
    return 'TODO!'


