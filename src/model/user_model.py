from datetime import datetime, timezone
from typing import Optional
from pydantic import EmailStr, field_validator
from sqlmodel import Field, SQLModel, func


class UserBase(SQLModel):
    username: str = Field(max_length=60, nullable=False)
    email: EmailStr
    cpf: str
    age: int = Field(nullable=False)
    is_active: bool = Field(default=True)

    @field_validator('cpf')
    @classmethod
    def validate_cpf(cls, v: str):
        if len(v) != 11 or not v.isdigit():
            raise ValueError('CPF inválido')
        return v


class UserCreate(UserBase):
    password: str = Field(max_length=255, nullable=False)


class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    cpf: str = Field(unique=True, index=True)
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        sa_column_kwargs={"server_default": func.now()}
    )
    password_hash: str = Field(max_length=255, nullable=False)


class UserRead(UserBase):
    id: int
    created_at: datetime
