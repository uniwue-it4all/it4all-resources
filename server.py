from flask import Flask, url_for, redirect

from blueprints.collection_routes import coll_blueprint
from blueprints.exercise_routes import exes_blueprint
from blueprints.tool_routes import tool_blueprint

app = Flask(__name__)

app.register_blueprint(tool_blueprint, url_prefix='/tools')

app.register_blueprint(coll_blueprint, url_prefix='/tools/<string:tool_id>')

app.register_blueprint(exes_blueprint, url_prefix='/tools/<string:tool_id>/collections/<int:coll_id>/')


@app.route('/')
def route_index():
    return redirect(url_for('tool_blueprint.route_tools'))


if __name__ == "__main__":
    app.debug = True
    app.config["JSON_SORT_KEYS"] = False
    app.run(host='0.0.0.0')
