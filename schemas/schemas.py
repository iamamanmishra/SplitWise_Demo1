from typing import Optional

from pydantic import BaseModel



class RegisterUser(BaseModel):
    user_id: str
    full_name: str
    password: str
    email: str


class createRoom_ipParams(BaseModel):
    user_id: Optional[str]=None
    room_name: Optional[str]=None
    currency: Optional[str]=None
    members: Optional[list]=None


class add_expense(BaseModel):
    room_id: Optional[str]=None
    paid_user_id: Optional[str]=None
    amount: Optional[float]=None
    expense_name: Optional[str]=None
    expense_date:Optional[str]=None
    fairsplit_members: Optional[list]=None
