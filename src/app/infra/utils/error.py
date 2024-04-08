from flask import abort, flash
from cowsay import func as cow_say


class Error(Exception):
    def __init__(
        self,
        ui_message: str = "Tivemos um problema grave 😨",
        error_message: str = "Internal Server Error",
        status_code: int = 500,
        should_abort=False,
    ) -> None:
        super().__init__(ui_message)
        self.message = ui_message

        if ui_message:
            flash(ui_message, "error")

        if error_message:
            cow_say(error_message)

        if should_abort:
            abort(status_code, error_message)
