from typing import Dict, Any, Union
from pathlib import Path
from yaml import YAMLObject

resource_base_dir: Path = Path.cwd() / 'resources'


class SemanticVersion:
    def __init__(self, major: int, minor: int, patch: int):
        self.major = major
        self.minor = minor
        self.patch = patch


# noinspection PyPep8Naming
class LongText(YAMLObject):
    yaml_tag = '!LongText'

    def __init__(self, relativePath: str):
        self.relativePath: str = relativePath

    def to_json(self) -> str:
        file_path: Path = resource_base_dir / self.relativePath
        return file_path.read_text()


# noinspection PyPep8Naming
class Exercise(YAMLObject):
    yaml_tag = '!Exercise'

    def __init__(
            self, id: int, collectionId: int, toolId: str, semanticVersion: SemanticVersion,
            title: str, author: str, text: Union[str, LongText], state: str, content: Any):
        self.id = id
        self.collectionId = collectionId
        self.toolId = toolId
        self.semanticVersion = semanticVersion
        self.title = title
        self.author = author
        self.text = text
        self.state = state
        self.content = content

    def to_json(self) -> Dict:
        return {
            'id': self.id,
            'collectionId': self.collectionId,
            'toolId': self.toolId,
            'semanticVersion': self.semanticVersion,
            'title': self.title,
            'author': self.author,
            'text': self.text if isinstance(self.text, str) else self.text.to_json(),
            'state': self.state,
            'content': self.content
        }
