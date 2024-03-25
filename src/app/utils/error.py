from flask import abort
from cowsay import func as cow_say


class Error(Exception):
    def __init__(self, message: str, status_code: int = 500, should_abort=True) -> None:
        cow_say(message)
        if should_abort:
            abort(status_code, message)
