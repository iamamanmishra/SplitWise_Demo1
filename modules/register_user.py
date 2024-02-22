import bcrypt

from modules.login_user import get_password_hash
from utils.constants import database_name, user_collection_name
from utils.dbOperations import find_single_data, insertData
from utils.utils import get_concatenated_datetime


def register_user(user_id, full_name, password, email):
    # create a unique user_id
    daytime_string = get_concatenated_datetime()
    unique_user_id = user_id + daytime_string
    # Hash the password
    hashed_password = get_password_hash(password)

    # check if the user_id exists in database or not
    data_existence = find_single_data(database_name, user_collection_name, {"user_id": user_id})
    if data_existence:
        print("User is already present in the database")
        return user_id
    else:
        # create a document
        dict_data = {
            "_id": unique_user_id,
            "user_id": user_id,
            "full_name": full_name,
            "password": hashed_password,
            "email": email
        }
        # insert data in database
        insertData(database_name, user_collection_name, dict_data)
        print("User registration successful")
        return unique_user_id
