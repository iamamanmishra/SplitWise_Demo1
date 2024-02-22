import bcrypt

from utils.constants import database_name, user_collection_name
from utils.dbOperations import insertData
from utils.utils import get_concatenated_datetime


def register_user(first_name, last_name, password, email):
    """
    Registers a new user.

    Parameters:
    - first_name (str): First name of the user.
    - last_name (str): Last name of the user.
    - password (str): Password for the user account.
    - email (str): Email address of the user.

    Returns:
    - str: Unique user ID upon successful registration.
    """
    try:
        # Create a unique user_id
        dayTime_string = get_concatenated_datetime()
        unique_user_id = first_name + dayTime_string

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
        return unique_user_id

    except Exception as e:
        print(f"User registration failed: {e}")
        return None
