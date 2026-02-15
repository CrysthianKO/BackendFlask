from errors.exception import UserAlreadyExistsError
from model.user_model import UserCreate
from repository.user_repository import UserRepository


def exists_user(repository: UserRepository, user_input: UserCreate):
    if repository.exists_by_email(user_input.email):
        raise UserAlreadyExistsError("A user with this email already exists.")

    if repository.exists_by_cpf(user_input.cpf):
        raise UserAlreadyExistsError("A user with this CPF already exists.")
