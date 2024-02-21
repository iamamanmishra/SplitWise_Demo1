from pydantic import BaseModel
from typing import Optional


class RegisterUser(BaseModel):
    user_id: str
    full_name: str
    password: str
    email: str



