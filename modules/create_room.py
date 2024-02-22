from utils.constants import database_name, room_collection_name
from utils.dbOperations import find_single_data, insertData
from utils.utils import checkUserExistanceInDB


def createRoom(admin_name, room_id, currency, members_array):
    members_array.append(str(admin_name))

    # check if room already exists
    dataExistance = find_single_data(database_name, room_collection_name, {"room_id": room_id})
    if dataExistance:
        print("Room is already created.....")
        return {"old_room": room_id}

    # check all members are present in userDatabase
    for user_id in members_array:
        if not checkUserExistanceInDB(user_id):
            print("added users are not found inside the existing database")
            return {"no_user": f"added users {user_id} are not found inside the existing database"}

    # create a document
    dict_data = {
        "admin_name": admin_name,
        "room_id": room_id,
        "currency": currency,
        "members_array": members_array
    }
    # insert data in database
    insertData(database_name, room_collection_name, dict_data)
    print("Room creation successful")
    return {"new_room": room_id}
