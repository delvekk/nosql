from pymongo import MongoClient


client = MongoClient('10.100.100.2')
base = client['TEST_DATABASE']
collection = base['TEST_COLLECTION']


for i in range(1500):
    collection.insert_one({'_id': i, 'column1': i*3, 'column2': i*4, 'column3': i*5, 'column4': i*6, 'column5': i*7, 'column6': i*8, 'column7': i*9, 'column8': i*10, 'column9': i*11})


