from dataclasses import dataclass
from pathlib import Path
from typing import List, Any, Dict

resource_base_dir: Path = Path.cwd() / 'resources'
schemas_path: Path = Path.cwd() / 'schemas'


def get_all_tool_ids() -> List[str]:
    return sorted([x.name for x in resource_base_dir.glob('*') if x.is_dir()])


def get_tool_dir(tool_id: str) -> Path:
    return resource_base_dir / tool_id


@dataclass()
class LongText:
    relative_path: str

    @staticmethod
    def from_json(json: Dict[str, Any]) -> 'LongText':
        return LongText(str(json['relativePath']))

    def to_json_dict(self) -> str:
        file_path: Path = resource_base_dir / self.relative_path
        return file_path.read_text()
