from __future__ import annotations


class IoError(Exception):
    """База ошибок IO-слоя."""


class UnsupportedFormatError(IoError):
    def __init__(self, key: str):
        super().__init__(f"Unsupported format: {key}")
        self.key = key


class ReadError(IoError):
    def __init__(self, path: str, original: Exception):
        super().__init__(f"Failed to read file: {path}. Cause: {original}")
        self.path = path
        self.original = original


class WriteError(IoError):
    def __init__(self, path: str, original: Exception):
        super().__init__(f"Failed to write file: {path}. Cause: {original}")
        self.path = path
        self.original = original


class DecodeError(IoError):
    def __init__(self, fmt: str, path: str, original: Exception):
        super().__init__(f"Failed to decode {fmt}: {path}. Cause: {original}")
        self.fmt = fmt
        self.path = path
        self.original = original


class EncodeError(IoError):
    def __init__(self, fmt: str, path: str, original: Exception):
        super().__init__(f"Failed to encode {fmt}: {path}. Cause: {original}")
        self.fmt = fmt
        self.path = path
        self.original = original
