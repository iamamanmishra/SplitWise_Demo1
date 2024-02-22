from utils.constants import database_name, expense_collection_name
from utils.dbOperations import find_data


# see transactions for a specific room
def show_transactions_under_room(room_id):
    found_room_details = find_data(database_name, expense_collection_name, {"room_id": room_id})
    # '_id': ObjectId('65d5e058e9081ae1afefaa4e') this is not iterable
    # removing the _id from each json present in the list
    for i in found_room_details:
        i.pop('_id',None)
    print(found_room_details)
    return found_room_details


