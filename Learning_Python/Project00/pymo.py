import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://lager:3#,2$,1!@cluster00.j1wxvz1.mongodb.net/?retryWrites=true&w=majority")
db = cluster["test"]
collection = db["test"]
collection1 = db["schedule"]
collection2 = db["requests"]

req1 = {'id': 'date1', 'name': 'user1', 'times': ['f','a']}
req2 = {'id': 'date1', 'name': 'user2', 'times': ['c','d']}
req3 = {'id': 'date2', 'name': 'user3', 'times': ['e','a']}
req4 = {'id': 'date2', 'name': 'user4', 'times': ['c','b']}


collection2brii.insert_many([req1, req2, req3, req4])