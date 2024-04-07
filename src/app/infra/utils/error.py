from flask import abort, flash
from cowsay import func as cow_say


class Error(Exception):
    def __init__(
        self,
        error_message: str,
        status_code: int = 500,
        ui_message="",
        should_abort=True,
    ) -> None:
        cow_say(error_message)
        if ui_message:
            flash(ui_message, "error")

        if should_abort:
            abort(status_code, error_message)
