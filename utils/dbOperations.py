import pymongo

# create a client
client = pymongo.MongoClient("mongodb://localhost:27017")
print("Conneted to DB")
print(client)

# # create a database
# db = client['arka_test']
# # without collection, db can't be created (manually tested)
# collection = db['test_datasets']
# # database is created, but we can't see it on mongo DB
# # atleast need a document inside collection to see it on DB
# sample_json = {'_id': 2, 'name': 'Arka', 'age': '29'}
# doc_dictionary = sample_json
# # if we wanna insert 1 dictionary, use insert-one
# # if we wanna insert list of dictionaries, use insert_many
# collection.insert_one(doc_dictionary)