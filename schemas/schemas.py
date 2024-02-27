from typing import Optional

from pydantic import BaseModel


class RegisterUser(BaseModel):
    user_name: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    password: Optional[str] = None
    email: Optional[str] = None


class LoginUser(RegisterUser):
    user_id: str


class createRoom_ipParams(BaseModel):
    room_name: Optional[str] = None
    currency: Optional[str] = None
    members: Optional[list] = None


class add_expense(BaseModel):
    room_id: Optional[str] = None
    amount: Optional[float] = None
    expense_name: Optional[str] = None
    expense_date: Optional[str] = None
    fairsplit_members: Optional[list] = None
