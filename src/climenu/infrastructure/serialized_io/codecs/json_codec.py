from __future__ import annotations

import json
from typing import Any

from .base import FormatCodec


class JsonCodec(FormatCodec):
    @property
    def format_name(self) -> str:
        return "json"

    @property
    def extensions(self) -> tuple[str, ...]:
        return (".json",)

    def loads(self, text: str) -> Any:
        return json.loads(text)

    def dumps(self, data: Any) -> str:
        return json.dumps(data, ensure_ascii=False, indent=2) + "\n"
