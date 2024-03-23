from models.user_model import UserModel


class AuthUser(UserModel):
    def __init__(self, user: UserModel) -> None:
        super().__init__(user.__dict__, user.id)
        self.is_active = True

    def get_id(self) -> UserModel:
        return self.id
