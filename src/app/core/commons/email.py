from typing import Literal
from re import compile, fullmatch

from core.commons.common import Common
from infra.repositories import professors_repository
from infra.utils.error import Error


class Email(Common):
    def __init__(self, value: str) -> None:
        self.value = value

    def validate(
        self,
        role: Literal["admin", "student", "professor"],
        exceptions: list[str] = [],
    ) -> bool:
        regex = compile(
            r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"
        )

        is_email = bool(fullmatch(regex, self.value))

        if not is_email:
            return False

        record = None

        if self.value not in exceptions:
            match role:
                case "professor":
                    record = professors_repository.get_professor_by_email(self.value)

        if record is not None:
            raise Error("E-mail já utilizado", 400)

        return bool(fullmatch(regex, self.value))

    def get_value(self):
        return self.value
