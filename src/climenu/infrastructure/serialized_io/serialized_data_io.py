from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from ._registry import _CodecRegistry
from .codecs.json_codec import JsonCodec
from .codecs.yaml_codec import YamlCodec
from .errors import DecodeError, EncodeError, ReadError, WriteError


def _default_registry() -> _CodecRegistry:
    # default codecs: YAML + JSON
    return _CodecRegistry.from_codecs([YamlCodec(), JsonCodec()])


@dataclass(frozen=True)
class SerializedDataIO:
    """
    Единый вход для чтения/записи сериализованных данных (YAML/JSON/…).
    Реестр и кодеки скрыты под капотом.
    """

    encoding: str = "utf-8"
    _registry: _CodecRegistry = field(default_factory=_default_registry, repr=False)

    def load(self, path: Path, *, fmt: str | None = None) -> Any:
        codec = self._select_codec(path, fmt)

        try:
            text = path.read_text(encoding=self.encoding)
        except Exception as e:
            raise ReadError(str(path), e) from e

        try:
            return codec.loads(text)
        except Exception as e:
            raise DecodeError(codec.format_name, str(path), e) from e

    def dump(self, path: Path, data: Any, *, fmt: str | None = None) -> None:
        codec = self._select_codec(path, fmt)

        try:
            text = codec.dumps(data)
        except Exception as e:
            raise EncodeError(codec.format_name, str(path), e) from e

        try:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding=self.encoding)
        except Exception as e:
            raise WriteError(str(path), e) from e

    def _select_codec(self, path: Path, fmt: str | None):
        if fmt:
            return self._registry.by_format(fmt)
        return self._registry.by_extension(path.suffix)
