from datetime import datetime

from utils.constants import database_name, user_collection_name
from utils.dbOperations import find_single_data


def get_concatenated_datetime():
    # Get the current date and time
    current_datetime = datetime.now()

    # Format the current date and time as a concatenated string
    concatenated_datetime = current_datetime.strftime("%Y%m%d%H%M%S")

    return str(concatenated_datetime)


def get_current_date():
    # Get the current date
    current_date = datetime.now().strftime("%Y-%m-%d")

    return current_date

def checkUserExistanceInDB(user_id):
    # check if the user_id exists in database or not
    dataExistance = find_single_data(database_name, user_collection_name, {"_id": user_id})
    if dataExistance:
        return True
    return False
