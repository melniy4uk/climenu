from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from climenu.infrastructure.serialized_io import SerializedDataIO
from climenu.infrastructure.serialized_io.errors import IoError

from .model import AppConfig


class ConfigError(Exception):
    pass


@dataclass(frozen=True)
class AppConfigIO:
    data_io: SerializedDataIO = SerializedDataIO()

    def load_or_default(self, path: Path) -> AppConfig:
        if not path.exists():
            return AppConfig()

        try:
            raw = self.data_io.load(path)
        except IoError as e:
            raise ConfigError(str(e)) from e

        if raw is None:
            return AppConfig()
        if not isinstance(raw, dict):
            raise ConfigError("Config must be a mapping (YAML/JSON object).")

        try:
            return AppConfig.model_validate(raw)
        except Exception as e:
            raise ConfigError(str(e)) from e
