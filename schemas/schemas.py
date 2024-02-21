from pydantic import BaseModel
from typing import Optional


class RegisterUser(BaseModel):
    user_id: str
    full_name: str
    password: str
    email: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    user_id: str or None = None


class User(BaseModel):
    user_id: str
    email: str or None = None
    full_name: str or None = None


class UserInDB(User):
    hashed_password: str
