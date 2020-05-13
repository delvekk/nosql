#!/usr/bin/python
import time
from pymongo import MongoClient
import mysql.connector as myc


connection = myc.connect(user='root', password='root', host='10.100.100.3', database='LAB')
cursor = connection.cursor()
cursor.execute('SELECT id, column1, column2, column3, column4, column5, column6, column7, column8, column9 FROM TEST_TABLE')

client = MongoClient('10.100.100.2:27017')
base = client['TEST_DATABASE']
collection = base['TEST_COLLECTION']

start_time = time.time()

for (id, column1, column2, column3, column4, column5, column6, column7, column8, column9) in cursor:
	collection.insert_one({'_id': id, 'column1': column1, 'column2': column2, 'column3': column3, 'column4': column4, 'column5': column5, 'column6': column6, 'column7': column7, 'column8': column8, 'column9': column9})
	
 
end_time = time.time()
result = end_time - start_time

print(f"PROCES KOPIOWANIA ZAJĄŁ: {result} sekund")



