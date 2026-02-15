from flask import Blueprint, jsonify, request
from sqlmodel import Session
from database import engine
from model.user_model import UserCreate
from repository.user_repository import UserRepository
from use_case.register_user import RegisterUserUseCase

user_router = Blueprint('user_router', __name__)


@user_router.post('/register')
def create_user():
    user_input = UserCreate.model_validate(request.get_json())

    with Session(engine) as session:
        repo = UserRepository(session)
        created_user = RegisterUserUseCase(repo).execute(user_input)

        return jsonify(created_user.model_dump()), 200


@user_router.get('/')
def get_users():

    return jsonify({"message": "Rota de teste funcionando!"})
