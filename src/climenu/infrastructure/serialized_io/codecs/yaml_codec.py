from __future__ import annotations

from typing import Any

from .base import FormatCodec


class YamlCodec(FormatCodec):
    @property
    def format_name(self) -> str:
        return "yaml"

    @property
    def extensions(self) -> tuple[str, ...]:
        return (".yaml", ".yml")

    def loads(self, text: str) -> Any:
        import yaml  # PyYAML

        return yaml.safe_load(text)

    def dumps(self, data: Any) -> str:
        import yaml  # PyYAML

        return yaml.safe_dump(data, allow_unicode=True, sort_keys=False)
