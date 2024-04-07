from datetime import date


class Age:
    def __init__(self, birthdate: date) -> None:
        today = date.today()
        self.age = (
            today.year
            - birthdate.year
            - ((today.month, today.day) < (birthdate.month, birthdate.day))
        )

    def get_value(self):
        return self.age
