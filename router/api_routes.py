from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from starlette import status
from starlette.responses import JSONResponse

from modules.login_user import authenticate_user, create_access_token, ACCESS_TOKEN_EXPIRES_MINUTES
from modules.register_user import register_user
from schemas.schemas import RegisterUser, Token

router = APIRouter(prefix='', tags=[], responses={404: {"description": "Not found"}})


@router.get("/")
async def health_check():
    return JSONResponse({'message': "health Check"})


@router.post("/register")
async def register(registerUser: RegisterUser):
    user_id = registerUser.user_id
    full_name = registerUser.full_name
    password = registerUser.password
    email = registerUser.email
    response_user_id = register_user(user_id, full_name, password, email)
    return JSONResponse({'user_id': response_user_id})


@router.post("/login", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Incorrect username or password",
                            headers={"www-Authenticate": "Bearer"})
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRES_MINUTES)
    access_token = create_access_token(data={"sub": user.user_id}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}
