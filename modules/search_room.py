# Get all room details for specific user
from modules.login import get_username_from_token
from utils.constants import database_name, room_collection_name
from utils.dbOperations import find_data


def getAllRooms(Authorization):
    # Extract admin name from the access token
    token = Authorization.split(" ")[1]
    user_id = get_username_from_token(token)
    room_details_list = find_data(database_name, room_collection_name, '')
    found_rooms = []
    for room_detailed_json in room_details_list:
        if 'members_array' in room_detailed_json:
            for members in room_detailed_json['members_array']:
                if members == user_id:
                    found_rooms.append(room_detailed_json['room_id'])

    print(found_rooms)
    return {f"User {user_id} found inside the following rooms":found_rooms}
