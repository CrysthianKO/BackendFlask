from sqlmodel import Session, select
from model.user_model import User


class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def exists_by_email(self, email: str) -> bool:
        statement = select(User).where(User.email == email)
        result = self.session.exec(statement).first()
        return result is not None

    def exists_by_cpf(self, cpf: str) -> bool:
        statement_cpf = select(User).where(User.cpf == cpf)
        result = self.session.exec(statement_cpf).first()
        return result is not None

    def save_user(self, user: User):
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
