from datetime import datetime, timedelta

import bcrypt
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

from utils.constants import database_name, user_collection_name, SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
from utils.dbOperations import find_data
from utils.logger_config import logger


# Function to authenticate the user
def authenticate_user(user_id: str, password: str):
    try:
        # Check user and password from the database
        user_data = find_data(database_name, user_collection_name, {"_id": user_id})
        if user_data:
            stored_user_id = user_data[0]['_id']
            stored_password = user_data[0]['password']

            # Decode the stored password from byte format
            hashed_password = stored_password[2:-1].encode('utf-8')
            logger.warning("password has been converted from string to byte format")

            # Check if the provided password matches the stored password
            if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
                print("Password matches")
                return stored_user_id
            else:
                logger.critical("Password doesn't match, returning None")
                print("Password does not match")
                return None
        else:
            print("User not found")
            logger.critical("Password doesn't match, returning None")
            return None
    except Exception as e:
        print(f"Error during user authentication: {e}")
        logger.error(f"Error during user authentication: {e}")
        return None


# Function to create an access token
def create_access_token(data: dict, expires_delta: timedelta = None):
    try:
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        logger.info("Access token created....")
        return encoded_jwt
    except Exception as e:
        print(f"Error creating access token: {e}")
        return None


# Function to handle user login
def do_login(user_id: str, password: str):
    try:
        user = authenticate_user(user_id, password)
        if not user:
            raise HTTPException(status_code=401, detail="Invalid username or password")

        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(data={"sub": user}, expires_delta=access_token_expires)

        if not access_token:
            raise HTTPException(status_code=500, detail="Failed to create access token")

        logger.info("Access token created....")

        return {"access_token": access_token, "token_type": "bearer"}
    except Exception as e:
        print(f"Error during user login: {e}")
        logger.error(f"Error during user login: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


# OAuth2 password bearer instance
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# Function to extract username from token
def get_username_from_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload.get("sub")
    except JWTError:
        logger.error("Invalid Token..")
        raise HTTPException(status_code=401, detail="Invalid token")

