class UsersRepository:
    def __init__(self, should_get_password=False) -> None:
        self.should_get_password = should_get_password
