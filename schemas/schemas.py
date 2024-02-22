from typing import Optional

from pydantic import BaseModel



class RegisterUser(BaseModel):
    user_id: Optional[str]=None
    full_name: Optional[str]=None
    password: Optional[str]=None
    email: Optional[str]=None


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
