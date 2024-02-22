from utils.constants import database_name, expense_collection_name
from utils.dbOperations import insertData


def addExpense(room_id,paid_user_id,amount,expense_name,fairsplit_members):
    # check if the user_id exists in following room

    # create a document
    sample_json = {
        "room_id": room_id,
        "paid_user_id": paid_user_id,
        "amount": amount,
        "expense_name": expense_name,
        "fairsplit_members": fairsplit_members
    }

    # insert data in database
    insertData(database_name, expense_collection_name, sample_json)
    print("Expense added successfully")

