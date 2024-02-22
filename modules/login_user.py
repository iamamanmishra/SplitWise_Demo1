from datetime import datetime, timedelta

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext

from schemas.schemas import TokenData, UserInDB
from utils.dbOperations import find_data

SECRET_KEY = "55254a50d2a4d6913267ced3045c322918c78a9cf4cd982d9ad8ec83c987e271"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRES_MINUTES = 30
DATABASE_NAME = 'FairSplit_Data'
COLLECTION_NAME = 'user_info_data'

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth_2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def get_user(user_id: str):
    db_query = find_data(DATABASE_NAME, COLLECTION_NAME, {"user_id": user_id})
    if user_id == db_query[0]['user_id']:
        user_data = db_query[0]
        return UserInDB(**user_data)


def authenticate_user(user_id: str, password: str):
    user = get_user(user_id)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


def create_access_token(data: dict, expires_delta: timedelta or None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)

    to_encode.update(({"exp": expire}))
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: str = Depends(oauth_2_scheme)):
    credential_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                         detail="Could not validate credentials",
                                         headers={"www-Authenticate": "Bearer"})
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credential_exception
        token_data = TokenData(user_id=user_id)
    except JWTError:
        raise credential_exception

    user = get_user(user_id=token_data.user_id)
    if user is None:
        raise credential_exception

    return user
