from dataclasses import is_dataclass, asdict as dataclasses_asdict
from typing import Dict, List

# noinspection Mypy
from animal_case import animalify
from flask import Flask, redirect
from flask import url_for, jsonify
from flask.json import JSONEncoder as FlaskJSONEncoder

from data.programming_data import programming_collections_and_exes
from data.regex.regex_data import regex_collections_and_exes
from data.sql_data import sql_collections_and_exes
from data.uml_data import uml_collections_and_exes
from data.web.web_data import web_collections_and_exes
from data.xml.xml_data import xml_collections_and_exes
from models.collection import CollectionAndExes, Exercise, ToolValues
from models.lesson import load_lesson, load_lessons

app = Flask(__name__)


class EnhancedJSONEncoder(FlaskJSONEncoder):
    def default(self, o):
        if is_dataclass(o):
            return dataclasses_asdict(o)
        return super().default(o)


all_tools: Dict[str, ToolValues] = {
    'programming': ToolValues(
        {pc.collection.id: pc for pc in programming_collections_and_exes},
        {}
    ),
    'regex': ToolValues(
        {rc.collection.id: rc for rc in regex_collections_and_exes},
        {}
    ),
    'rose': ToolValues({}, {}),
    'sql': ToolValues(
        {sc.collection.id: sc for sc in sql_collections_and_exes},
        {}
    ),
    'uml': ToolValues(
        {uc.collection.id: uc for uc in uml_collections_and_exes},
        {}
    ),
    'web': ToolValues(
        {wc.collection.id: wc for wc in web_collections_and_exes},
        {}
    ),
    'xml': ToolValues(
        {xc.collection.id: xc for xc in xml_collections_and_exes},
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
    tool_values: ToolValues = all_tools[tool_id]

    return jsonify(
        animalify({
            'parent_url': url_for('route_tools', _external=True),
            'tool_id': tool_id,
            'collections': {
                'count': len([co for co in tool_values.collections]),
                'all': url_for('route_collections', tool_id=tool_id, _external=True),
                'single': [
                    {
                        'id': collection.collection.id,
                        'url': url_for('route_collection', tool_id=tool_id, coll_id=collection.collection.id,
                                       _external=True)
                    } for collection in tool_values.collections.values()
                ]
            },
            'lessons': {
                'count': len([le for le in tool_values.lessons]),
                'all': url_for('route_lessons', tool_id=tool_id, _external=True),
                'single': [
                    {
                        'id': lesson.id,
                        'url': url_for('route_lesson', tool_id=tool_id, lesson_id=lesson.id, _external=True)
                    } for lesson in tool_values.lessons.values()
                ]
            }
        })
    )


# collection routes

@app.route('/tools/<string:tool_id>/collections')
def route_collections(tool_id: str):
    return jsonify(
        animalify({
            'parent_url': url_for('route_tool', tool_id=tool_id, _external=True),
            'collections': [x.collection for x in all_tools[tool_id].collections.values()]
        })
    )


@app.route('/tools/<string:tool_id>/collections/<int:coll_id>')
def route_collection(tool_id: str, coll_id: int):
    coll_and_ex: CollectionAndExes = all_tools[tool_id].collections[coll_id]

    return jsonify(
        animalify({
            'parent_url': url_for('route_collections', tool_id=tool_id, _external=True),
            'meta_data': coll_and_ex.collection,
            'exercises': {
                'count': -1,
                'all': url_for('route_exercises', tool_id=tool_id, coll_id=coll_id, _external=True),
                'single': [
                    {
                        'id': ex_id,
                        'url': url_for(
                            'route_exercise', tool_id=tool_id, coll_id=coll_id, ex_id=ex_id, _external=True
                        ),
                    } for ex_id in coll_and_ex.exercises.keys()
                ]
            }
        })
    )


@app.route('/tools/<string:tool_id>/collections/<int:coll_id>/exercises/')
def route_exercises(tool_id: str, coll_id: int):
    exercises: List[Exercise] = list(all_tools[tool_id].collections[coll_id].exercises.values())

    return jsonify(
        animalify({
            'parent_url': url_for('route_collection', tool_id=tool_id, coll_id=coll_id, _external=True),
            'exercises': exercises
        })
    )


@app.route('/tools/<string:tool_id>/collections/<int:coll_id>/exercises/<int:ex_id>')
def route_exercise(tool_id: str, coll_id: int, ex_id: int):
    exercise: Exercise = all_tools[tool_id].collections[coll_id].exercises[ex_id]

    return jsonify(
        animalify({
            'parent_url': url_for('route_collection', tool_id=tool_id, coll_id=coll_id, _external=True),
            'exercise': exercise
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
    app.json_encoder = EnhancedJSONEncoder
    app.run(host='0.0.0.0')
