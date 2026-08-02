from __future__ import annotations

import json
from pathlib import Path
from tempfile import NamedTemporaryFile

from .model import Character


class CharacterRepository:
    """Versioned JSON persistence for character records."""

    def __init__(self, root: Path | str) -> None:
        self.root = Path(root)
        self.root.mkdir(parents=True, exist_ok=True)

    def path_for(self, character_id: str) -> Path:
        if not character_id or any(ch in character_id for ch in ("/", "\\", "..")):
            raise ValueError("character_id must be a simple file-safe identifier")
        return self.root / f"{character_id}.json"

    def save(self, character: Character) -> Path:
        destination = self.path_for(character.character_id)
        payload = json.dumps(character.to_dict(), indent=2, sort_keys=True) + "\n"

        with NamedTemporaryFile(
            "w",
            encoding="utf-8",
            dir=self.root,
            prefix=f".{character.character_id}.",
            suffix=".tmp",
            delete=False,
        ) as temporary:
            temporary.write(payload)
            temporary.flush()
            temporary_path = Path(temporary.name)

        temporary_path.replace(destination)
        return destination

    def load(self, character_id: str) -> Character:
        path = self.path_for(character_id)
        with path.open("r", encoding="utf-8") as source:
            data = json.load(source)
        return Character.from_dict(data)

    def exists(self, character_id: str) -> bool:
        return self.path_for(character_id).is_file()

    def list_ids(self) -> list[str]:
        return sorted(path.stem for path in self.root.glob("*.json") if path.is_file())
