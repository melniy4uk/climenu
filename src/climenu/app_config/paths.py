from __future__ import annotations

import os
from pathlib import Path

APP_NAME = "climenu"


def default_config_path() -> Path:
    base = Path(os.environ.get("XDG_CONFIG_HOME", Path.home() / ".config")).expanduser()
    return base / APP_NAME / "config.yaml"
