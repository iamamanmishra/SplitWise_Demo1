import logging
from modules.login import get_username_from_token
from utils.constants import database_name, room_collection_name
from utils.dbOperations import find_data
from utils.logger_config import logger

def getAllRooms(Authorization):
    try:
        # Extract admin name from the access token
        token = Authorization.split(" ")[1]
        user_id = get_username_from_token(token)

        # Retrieve all room details
        room_details_list = find_data(database_name, room_collection_name, '')

        found_rooms = []

        # Check if the user is a member of any room
        for room_detailed_json in room_details_list:
            if 'members_array' in room_detailed_json:
                for member in room_detailed_json['members_array']:
                    if member == user_id:
                        found_rooms.append(room_detailed_json['room_id'])

        logger.info("getAllRooms function executed successfully")
        return {f"User {user_id} found inside the following rooms": found_rooms}

    except Exception as e:
        # Log any exceptions
        logger.exception("An error occurred in getAllRooms function")
        return {"error": "An error occurred while fetching room details"}
