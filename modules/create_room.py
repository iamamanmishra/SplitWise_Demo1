from modules.login import get_username_from_token
from utils.constants import database_name, room_collection_name
from utils.dbOperations import find_single_data, insertData
from utils.utils import checkUserExistanceInDB
from fastapi import HTTPException


def createRoom(Authorization, room_id, currency, members_array):
    try:
        # Extract admin name from the access token
        token = Authorization.split(" ")[1]
        admin_name = get_username_from_token(token)
        # add admin in member array if not present
        if str(admin_name) not in members_array:
            members_array.append(str(admin_name))

        # Check if the room already exists
        dataExistence = find_single_data(database_name, room_collection_name, {"room_id": room_id})
        if dataExistence:
            print("Room is already created")
            return {"old_room": room_id}

        # Check if all members are present in the user database
        for user_id in members_array:
            if not checkUserExistanceInDB(user_id):
                print(f"User {user_id} is not found in the database")
                return {"no_user": f"User {user_id} is not found in the database"}

        # Create a document
        room_document = {
            "admin_name": admin_name,
            "room_id": room_id,
            "currency": currency,
            "members_array": members_array
        }
        # Insert data into the database
        insertData(database_name, room_collection_name, room_document)
        print("Room creation successful")
        return {"new_room": room_id}
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
