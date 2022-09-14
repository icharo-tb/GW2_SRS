import pymongo
import sys

try:
    client = pymongo.MongoClient('mongodb://localhost:27017/')
except Exception as e:
    print('Connection could not be done' + str(e))
    sys.exit()

db = client['GW2_SRS']
collection = db['players_info']

mongo_insert = collection.insert_many()