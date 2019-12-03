from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Optional

resource_base_dir: Path = Path.cwd() / 'resources'
schemas_path: Path = Path.cwd() / 'schemas'


@dataclass()
class LongText:
    relative_path: str

    @staticmethod
    def from_yaml(yaml: Dict[str, Any]) -> Optional['LongText']:
        try:
            return LongText(yaml['relativePath'])
        except:
            return None

    def to_json(self) -> str:
        file_path: Path = resource_base_dir / self.relative_path
        return file_path.read_text()
