import bcrypt

from utils.constants import database_name, user_collection_name
from utils.dbOperations import insertData, find_data
from utils.logger_config import logger
from utils.utils import get_concatenated_datetime


def register_user(unique_user_id, first_name, last_name, password, email):
    """
    Registers a new user.

    Parameters:
    - unique_user_id (str): First name of the user.
    - first_name (str): First name of the user.
    - last_name (str): Last name of the user.
    - password (str): Password for the user account.
    - email (str): Email address of the user.

    Returns:
    - str: Unique user ID upon successful registration.
    """
    logger.info("Calling register_user function..")
    try:
        # check if user_id,email is not present on existing database
        user_database = find_data(database_name, user_collection_name, '')

        for user_json in user_database:

            if unique_user_id == user_json['_id']:
                return {"message": f"user_name: {unique_user_id} already exists"}
            if email == user_json['email']:

                return {"message": f"Email: {email} already exists"}

        # Hash the password
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        # Convert the hashed password to string format
        str_pwd = str(hashed_password)

        # Create a document for the new user
        user_document = {
            "_id": unique_user_id,
            "first_name": first_name,
            "last_name": last_name,
            "password": str_pwd,
            "email": email
        }

        # Insert the user data into the database
        insertData(database_name, user_collection_name, user_document)
        print("User registration successful")
        logger.info("register_user function executed successfully..")
        return {"message":f"User {unique_user_id} registration successful"}

    except Exception as e:
        print(f"User registration failed: {e}")
        logger.error(f"error inregister_user function, error {e}")
        return None
