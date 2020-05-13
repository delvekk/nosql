from pymongo import MongoClient
import time
import random

client1 = MongoClient('10.100.100.2')
base1 = client1['TEST_DATABASE']
collection1 = base1['TEST_COLLECTION']

client2 = MongoClient('10.100.100.3')
base2 = client2['TEST_DATABASE']
collection2 = base2['TEST_COLLECTION']


collection1_size = collection1.count_documents({})
collection2_size = collection2.count_documents({})

start_time = time.time()
while collection2_size < collection1_size:
    random_record_id = random.randint(0, collection1_size - 1)

    if collection2.count_documents({ '_id': random_record_id }, limit = 1) == 0:
        random_record = collection1.find_one({'_id': random_record_id})
        collection2.insert_one(random_record)
        collection2_size += 1

end_time = time.time() - start_time

print(f"Kopiowanie {collection1_size} rekordow trwalo {end_time} sekund. W drugiej bazie znajduje sie {collection2_size} rekordow")
