from flask import Flask
from sqlmodel import Session
from database import engine
from repository.user_repository import UserRepository

SQLModel.metadata.create_all(engine)

app = Flask(__name__)

if __name__ == "__main__":

    with Session(engine) as session:
        repo = UserRepository(session)
        repo.exists_by_email('email@email.com')
        
    app.run()