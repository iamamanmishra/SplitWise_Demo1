from modules.login import get_username_from_token
from utils.constants import database_name, expense_collection_name
from utils.dbOperations import find_data


def check_User_spendings(Authorization):
    # Extract admin name from the access token
    token = Authorization.split(" ")[1]
    paid_user_id = get_username_from_token(token)

    # iterate via all the transactions and check if user has made the transactions
    user_transactions_list = find_data(database_name, expense_collection_name, {"paid_user_id": paid_user_id})
    for i in user_transactions_list:
        i.pop('_id', None)
    print(user_transactions_list)

    # calculate spending
    user_spending_list=[]

    total_spending=0
    for expense_dic in user_transactions_list:
        total_spending=total_spending+expense_dic['amount']
        user_json={
            "room_id":expense_dic['room_id'],
            "spent_amount":expense_dic['amount'],
            "expense_name": expense_dic['expense_name']
        }
        user_spending_list.append(user_json)
    return {
        "total_spending":total_spending,
        "spending_details":user_spending_list
    }

# this code can be improved
# user should see how much he/she is spending on each room
# instead of seperate spending, user should see the total amount what is spent on a individual room

