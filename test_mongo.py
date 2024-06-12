import mongomock
import pandas as pd

# Test setup: create a mock MongoDB database
def setup_mock_mongo():
    client = mongomock.MongoClient()
    db = client['test_db']
    collection = db['users']
    collection.insert_many([
        {'name': 'Sahil', 'age': 22},
        {'name': 'sa', 'age': 35},
        {'name': 'hi', 'age': 45},
        {'name': 'ls', 'age': 55}
    ])
    return db

def query_mongo(db, collection_name, query):
    collection = db[collection_name]
    cursor = collection.find(query)
    df = pd.DataFrame(list(cursor))
    return df

db = setup_mock_mongo()
query = {'name': 'Sahil'}
result = query_mongo(db, 'users', query)
print(result)
