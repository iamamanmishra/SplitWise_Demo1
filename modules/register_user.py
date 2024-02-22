import bcrypt

from utils.constants import database_name, user_collection_name
from utils.dbOperations import find_single_data, insertData
from utils.utils import get_concatenated_datetime


def register_user(user_id, full_name, password, email):
    # create a unique user_id
    dayTime_string = get_concatenated_datetime()
    unique_user_id=user_id+dayTime_string
    # Hash the password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    # storing the Bcrypt password as string format
    # mongoDb saves the binary data in diff way
    str_pwd=str(hashed_password)
    print(str_pwd)

    # check if the user_id exists in database or not
    dataExistance=find_single_data(database_name,user_collection_name,{"user_id": user_id})
    if dataExistance:
        print( "User is already present in the database")
        return user_id
    else:
        # create a document
        dict_data = {
            "_id":unique_user_id,
            "user_id": unique_user_id,
            "full_name": full_name,
            "password": str_pwd,
            "email": email
        }
        # insert data in database
        insertData(database_name, user_collection_name, dict_data)
        print("User registration successful")
        return unique_user_id





