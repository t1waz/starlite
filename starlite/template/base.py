from typing import Any, Dict, List, Optional, TypeVar, Union

from pydantic import DirectoryPath
from typing_extensions import Protocol, runtime_checkable


@runtime_checkable
class AbstractTemplate(Protocol):  # pragma: no cover
    def render(self, **context: Optional[Dict[str, Any]]) -> str:
        """Returns the rendered template as a string"""
        ...


T = TypeVar("T", bound=AbstractTemplate, covariant=True)


@runtime_checkable
class TemplateEngineProtocol(Protocol[T]):  # pragma: no cover
    def __init__(self, directory: Union[DirectoryPath, List[DirectoryPath]]) -> None:
        """Builds a template engine."""
        ...

    def get_template(self, name: str) -> T:
        """Loads the template with name and returns it."""
        ...
