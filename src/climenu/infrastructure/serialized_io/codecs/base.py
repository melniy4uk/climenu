from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class FormatCodec(ABC):
    """Контракт формата: text <-> python data."""

    @property
    @abstractmethod
    def format_name(self) -> str: ...

    @property
    @abstractmethod
    def extensions(self) -> tuple[str, ...]: ...

    @abstractmethod
    def loads(self, text: str) -> Any: ...

    @abstractmethod
    def dumps(self, data: Any) -> str: ...
