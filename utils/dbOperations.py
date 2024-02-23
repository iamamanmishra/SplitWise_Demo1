import pymongo
from pymongo import MongoClient

from utils.constants import mongoDBConnection

# create a client
client = pymongo.MongoClient(mongoDBConnection)
print("Connected to DB")


def insertData(database_name, collection_name, dict_data):
    # Access database
    db = client[database_name]
    # Access collection
    collection = db[collection_name]
    # Insert data into MongoDB
    result = collection.insert_one(dict_data)
    print("Data inserted.Inserted document ID:", result.inserted_id)
    return result.inserted_id


def find_data(database_name, collection_name, dict_data_query):
    # Access database
    db = client[database_name]
    # Access collection
    collection = db[collection_name]
    # Perform the search
    results = collection.find(dict_data_query)
    found_data_dict_list = []
    for result in results:
        # print(result)
        found_data_dict_list.append(result)
    return found_data_dict_list


def find_single_data(database_name, collection_name, dict_data_query):
    # Access database
    db = client[database_name]
    # Access collection
    collection = db[collection_name]
    # Perform the search
    if collection.find_one(dict_data_query):
        return True
    return False
