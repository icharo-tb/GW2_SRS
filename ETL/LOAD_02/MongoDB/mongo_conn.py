import pymongo
import sys


def load_mongo(jsonFile):
    try:
        client = pymongo.MongoClient('mongodb://localhost:27017/')
    except Exception as e:
        print('Connection could not be done' + str(e))
        sys.exit()

    db = client['GW2_SRS']
    collection = db['players_info']

    return collection.insert_one(jsonFile)
pass