from re import compile, fullmatch

from core.commons.common import Common


class Email(Common):
    def __init__(self, value: str) -> None:
        self.value = value

    def validate(self) -> bool:
        regex = compile(
            r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"
        )

        return bool(fullmatch(regex, self.value))
