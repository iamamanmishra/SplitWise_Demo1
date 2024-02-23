from modules.login import get_username_from_token
from utils.constants import database_name, expense_collection_name
from utils.dbOperations import insertData
from utils.logger_config import logger


def addExpense(room_id, Authorization, amount, expense_name, fairsplit_members):
    try:
        # Extract admin name from the access token
        token = Authorization.split(" ")[1]
        paid_user_id = get_username_from_token(token)

        # Add logged-in user to the members list
        fairsplit_members.append(paid_user_id)

        # Create a document
        expense_data = {
            "room_id": room_id,
            "paid_user_id": paid_user_id,
            "amount": amount,
            "expense_name": expense_name,
            "fairsplit_members": fairsplit_members
        }

        # Insert data into the database
        insertData(database_name, expense_collection_name, expense_data)
        logger.info("Expense added successfully")
        print("Expense added successfully")

    except Exception as e:
        logger.exception(f"An error occurred while adding expense: {e}")
        print(f"An error occurred while adding expense: {e}")
