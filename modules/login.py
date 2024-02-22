# Constants
from datetime import datetime, timedelta

import bcrypt
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

from utils.constants import database_name, user_collection_name, SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
from utils.dbOperations import find_data


# authenticate the user
def authenticate_user(user_id, password):
    try:
        # check user and password from DB
        json = find_data(database_name, user_collection_name, {"user_id": user_id})
        user_id = json[0]['user_id']
        pwd = json[0]['password']
        # while reading remove 1st and last char from database  pwd[2:-1]
        # converting the string into byte format
        hashed_password = pwd[2:-1].encode('utf-8')
        if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
            print("Password matches")
            return user_id
        else:
            print("Password does not match")
            return None
    except:
        return None


def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def doLogin(user_id, password):
    user = authenticate_user(user_id, password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_username_from_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload.get("sub")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

# x = doLogin(user_id='test12320240222152020', password="testpassword123")
# print(x)
# x=get_username_from_token(token=token)
