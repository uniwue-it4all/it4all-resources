from dataclasses import dataclass
from typing import Dict, Any, List

from animal_case import animalify
from flask import Flask, redirect
from flask import url_for, jsonify

from data.programming_data import programming_collections
from data.regex_data import regex_collections
from data.sql_data import sql_collections
from data.uml_data import uml_collections
from data.web_data import web_collections
from data.xml_data import xml_collections
from models.collection import Collection, Exercise
from models.exercise import load_exercise, load_exercises
from models.lesson import load_lesson, load_lessons

app = Flask(__name__)


@dataclass()
class CollAndExes:
    collection: Collection
    exercises: List[Exercise]


@dataclass()
class ToolValues:
    collections: Dict[int, CollAndExes]
    lessons: Dict[int, Any]


all_tools: Dict[str, ToolValues] = {
    'programming': ToolValues(
        {pc['id']: CollAndExes(pc, []) for pc in programming_collections},
        {}
    ),
    'regex': ToolValues(
        {rc['id']: CollAndExes(rc, []) for rc in regex_collections},
        {}
    ),
    'rose': ToolValues({}, {}),
    'sql': ToolValues(
        {sc['id']: CollAndExes(sc, []) for sc in sql_collections},
        {}
    ),
    'uml': ToolValues(
        {uc['id']: CollAndExes(uc, []) for uc in uml_collections},
        {}
    ),
    'web': ToolValues(
        {wc['id']: CollAndExes(wc, []) for wc in web_collections},
        {}
    ),
    'xml': ToolValues(
        {xc['id']: CollAndExes(xc, []) for xc in xml_collections},
        {}
    ),
}


@app.route('/')
def route_index():
    return redirect(url_for('route_tools'))


@app.route('/tools')
def route_tools():
    return jsonify(
        animalify({
            'tools': [
                {
                    'id': tool_id,
                    'tool_url': url_for('route_tool', tool_id=tool_id, _external=True)
                } for tool_id in all_tools.keys()
            ]
        })
    )


@app.route('/tools/<string:tool_id>')
def route_tool(tool_id: str):
    tool_values = all_tools[tool_id]

    return jsonify(
        animalify({
            'parent_url': url_for('route_tools', _external=True),
            'tool_id': tool_id,
            'collections': {
                'count': len([co for co in tool_values.collections]),
                'all': url_for('route_collections', tool_id=tool_id, _external=True),
                'single': [
                    {
                        'id': collection.collection['id'],
                        'url': url_for('route_collection', tool_id=tool_id, coll_id=collection.collection['id'],
                                       _external=True)
                    } for collection in tool_values.collections.values()
                ]
            },
            'lessons': {
                'count': len([le for le in tool_values.lessons]),
                'all': url_for('route_lessons', tool_id=tool_id, _external=True),
                'single': [
                    {
                        'id': lesson['id'],
                        'url': url_for('route_lesson', tool_id=tool_id, lesson_id=lesson['id'], _external=True)
                    } for lesson in tool_values.lessons.values()
                ]
            }
        })
    )


# collection routes

@app.route('/tools/<string:tool_id>/collections')
def route_collections(tool_id: str):
    collections: List[Collection] = [x.collection for x in all_tools[tool_id].collections.values()]
    return jsonify(
        animalify({
            'parent_url': url_for('route_tool', tool_id=tool_id, _external=True),
            'collections': collections
        })
    )


@app.route('/tools/<string:tool_id>/collections/<int:coll_id>')
def route_collection(tool_id: str, coll_id: int):
    coll_and_ex = all_tools[tool_id].collections[coll_id]

    return jsonify(
        animalify({
            'parent_url': url_for('route_collections', tool_id=tool_id, _external=True),
            'meta_data': coll_and_ex.collection,
            'exercises': {
                'count': -1,
                'all': url_for('route_exercises', tool_id=tool_id, coll_id=coll_id, _external=True),
                'single': [
                    {
                        'id': ex['id'],
                        'url': url_for(
                            'route_exercise', tool_id=tool_id, coll_id=coll_id, ex_id=ex['id'], _external=True
                        ),
                    } for ex in coll_and_ex.exercises
                ]
            }
        })
    )


@app.route('/tools/<string:tool_id>/collections/<int:coll_id>/exercises/')
def route_exercises(tool_id: str, coll_id: int):
    return jsonify(
        animalify({
            'parent_url': url_for('route_collection', tool_id=tool_id, coll_id=coll_id, _external=True),
            'exercises': load_exercises(tool_id, coll_id)
        })
    )


@app.route('/tools/<string:tool_id>/collections/<int:coll_id>/exercises/<int:ex_id>')
def route_exercise(tool_id: str, coll_id: int, ex_id: int):
    return jsonify(
        animalify({
            'parent_url': url_for('route_collection', tool_id=tool_id, coll_id=coll_id, _external=True),
            'exercise': load_exercise(tool_id, coll_id, ex_id)
        })
    )


# lesson routes

@app.route('/tools/<string:tool_id>/lessons')
def route_lessons(tool_id: str):
    return jsonify(
        animalify({
            'parent_url': url_for('route_tool', tool_id=tool_id),
            'lessons': load_lessons(tool_id)
        })
    )


@app.route('/tools/<string:tool_id>/lessons/<int:lesson_id>')
def route_lesson(tool_id: str, lesson_id: int):
    return jsonify(
        animalify({
            'parent_url': url_for('route_lessons', tool_id=tool_id, _external=True),
            'metaData': load_lesson(tool_id, lesson_id)
        })
    )


if __name__ == "__main__":
    app.debug = True
    app.config["JSON_SORT_KEYS"] = False
    app.run(host='0.0.0.0')
