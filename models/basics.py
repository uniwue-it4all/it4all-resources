from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Optional, List

resource_base_dir: Path = Path.cwd() / 'resources'
schemas_path: Path = Path.cwd() / 'schemas'


def get_all_tool_ids() -> List[str]:
    return sorted([x.name for x in resource_base_dir.glob('*') if x.is_dir()])


@dataclass()
class LongText:
    relative_path: str

    @staticmethod
    def from_yaml(yaml: Dict[str, Any]) -> Optional['LongText']:
        # noinspection PyBroadException
        try:
            return LongText(yaml['relativePath'])
        except Exception as e:
            print(e)
            return None

    def to_json(self) -> str:
        file_path: Path = resource_base_dir / self.relative_path
        return file_path.read_text()
