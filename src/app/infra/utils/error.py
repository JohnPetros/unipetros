from cowsay import func as cow_say


class Error(Exception):
    def __init__(
        self,
        ui_message: str = "Tivemos um problema grave 😨",
        internal_message: str = "Internal Server Error",
        status_code: int = 500,
    ) -> None:
        super().__init__(ui_message)
        self.ui_message = ui_message
        self.internal_message = internal_message
        self.status_code = status_code

        if internal_message:
            cow_say(internal_message)
