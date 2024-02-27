from modules.login import get_username_from_token
from utils.constants import database_name, expense_collection_name, room_collection_name
from utils.dbOperations import insertData, find_data
from utils.logger_config import logger
from utils.utils import get_concatenated_datetime
import random


def addExpense(room_id, Authorization, amount, expense_name, fairsplit_members):
    try:
        # Create a unique transaction_id
        dayTime_string = get_concatenated_datetime()
        random_number = random.randint(1, 100)
        unique_transaction_id = "transaction_" + str(random_number)+"_" + dayTime_string

        # Extract admin name from the access token
        token = Authorization.split(" ")[1]
        paid_user_id = get_username_from_token(token)

        # check if user is part of that particular room
        found_room_details = find_data(database_name, room_collection_name, {"room_id": room_id})
        room_members_list = found_room_details[0]['members_array']
        print(room_members_list)
        bol_result = all(element in room_members_list for element in fairsplit_members)
        if not bol_result:
            return {"message": f"Members are not present in room: {room_id}"}

        # Add logged-in user to the members list
        fairsplit_members.append(paid_user_id)

        # Create a document
        expense_data = {
            "_id": unique_transaction_id,
            "room_id": room_id,
            "paid_user_id": paid_user_id,
            "amount": amount,
            "expense_name": expense_name,
            "fairsplit_members": list(set(fairsplit_members))
            # to remove duplicate # ane user can't be added multiple time
        }

        # Insert data into the database
        insertData(database_name, expense_collection_name, expense_data)
        logger.info("Expense added successfully")
        print("Expense added successfully")
        return {"message": "Expense added successfully"}

    except Exception as e:
        logger.exception(f"An error occurred while adding expense: {e}")
        print(f"An error occurred while adding expense: {e}")
