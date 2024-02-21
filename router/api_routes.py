

from fastapi import APIRouter
from starlette.responses import JSONResponse

from modules.register_user import register_user
from schemas.schemas import RegisterUser

router = APIRouter(prefix='', tags=[], responses={404: {"description": "Not found"}})


@router.get("/")
async def health_check():
    return JSONResponse({'message': "health Check"})

@router.post("/register")
async def register(registerUser:RegisterUser):
    user_id=registerUser.user_id
    full_name=registerUser.full_name
    password=registerUser.password
    email=registerUser.email
    response_user_id=register_user(user_id, full_name, password, email)
    return JSONResponse({'user_id': response_user_id})