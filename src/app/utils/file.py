from pathlib import Path
from utils.error import Error


class File:
    def __init__(self, folder, filename) -> None:
        self.path = Path(f"{folder}/{filename}")

    def read_text(self) -> str:
        try:
            return self.path.read_text(encoding="utf-8")
        except Exception as exception:
            raise Error(
                f"Failed to read {self.path.absolute()} file. Error: {exception}"
            ) from exception
