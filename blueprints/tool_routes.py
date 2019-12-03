from pathlib import Path
from typing import List, Dict

from flask import Blueprint, request, url_for, jsonify, redirect

from models.basics import resource_base_dir

tool_blueprint: Blueprint = Blueprint('tool_blueprint', __name__)


def tool_exists(tool_id: str) -> bool:
    tool_path: Path = resource_base_dir / tool_id
    return tool_path.exists() and tool_path.is_dir()


@tool_blueprint.route('/')
def route_tools():
    tool_ids: List[str] = sorted([x.name for x in resource_base_dir.glob('*') if x.is_dir()])

    tools: List[Dict[str, str]] = [
        {
            'id': tool_id,
            'toolUrl': request.host_url[:-1] + url_for('tool_blueprint.route_tool', tool_id=tool_id)
        } for tool_id in tool_ids
    ]

    return jsonify({'tools': tools})


@tool_blueprint.route('/<string:tool_id>')
def route_tool(tool_id: str):
    parent_url: str = url_for('tool_blueprint.route_tools')

    if not tool_exists(tool_id):
        return redirect(parent_url)

    return jsonify({
        'parentUrl': request.host_url[:-1] + parent_url,
        'tool_id': tool_id,
        'collectionIdsUrl': request.host_url[:-1] + url_for('coll_blueprint.route_collection_ids', tool_id=tool_id),
        'collectionsUrl': request.host_url[:-1] + url_for('coll_blueprint.route_collections', tool_id=tool_id)
    })
