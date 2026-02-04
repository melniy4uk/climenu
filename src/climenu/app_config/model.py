from __future__ import annotations

from pathlib import Path
from pydantic import BaseModel, ConfigDict, Field, field_validator


class AppConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    commands_dir: Path = Field(default=Path("~/.config/climenu/commands"))

    @field_validator("commands_dir", mode="before")
    @classmethod
    def _to_path(cls, v):
        return Path(v).expanduser()
