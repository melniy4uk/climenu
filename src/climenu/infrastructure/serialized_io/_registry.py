from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

from .codecs.base import FormatCodec
from .errors import UnsupportedFormatError


@dataclass(frozen=True)
class _CodecRegistry:
    _by_format: dict[str, FormatCodec]
    _by_ext: dict[str, FormatCodec]

    @classmethod
    def from_codecs(cls, codecs: Iterable[FormatCodec]) -> "_CodecRegistry":
        by_format: dict[str, FormatCodec] = {}
        by_ext: dict[str, FormatCodec] = {}

        for c in codecs:
            by_format[c.format_name.lower()] = c
            for ext in c.extensions:
                by_ext[ext.lower()] = c

        return cls(_by_format=by_format, _by_ext=by_ext)

    def by_format(self, fmt: str) -> FormatCodec:
        codec = self._by_format.get(fmt.lower())
        if codec is None:
            raise UnsupportedFormatError(fmt)
        return codec

    def by_extension(self, ext: str) -> FormatCodec:
        codec = self._by_ext.get(ext.lower())
        if codec is None:
            raise UnsupportedFormatError(ext)
        return codec
