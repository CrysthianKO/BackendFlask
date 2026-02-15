import bcrypt
from model.user_model import User, UserCreate, UserRead
from .utils import exists_user
from repository.user_repository import UserRepository


class RegisterUserUseCase:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def execute(self, user_input: UserCreate) -> UserRead:

        exists_user(self.repository, user_input)

        bytes_password = user_input.password.encode('utf-8')
        hash_password = bcrypt.hashpw(bytes_password, bcrypt.gensalt())
        hash_string = hash_password.decode('utf-8')

        new_user_db = User(
            **user_input.model_dump(exclude={"password"}),
            password_hash=hash_string
        )

        self.repository.save_user(new_user_db)

        user_read_db = UserRead.model_validate(new_user_db)

        return user_read_db
