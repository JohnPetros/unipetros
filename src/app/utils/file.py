from pathlib import Path
from utils.app_error import AppError


class File:
    def __init__(self, folder, filename) -> None:
        self.path = Path(f"{folder}/{filename}")

    def read(self) -> str:
        try:
            return self.path.read_text(encoding="utf-8")
        except Exception as exception:
            raise AppError(
                f"Failed to read {self.path.absolute()} file. Error: {exception}"
            ) from exception
