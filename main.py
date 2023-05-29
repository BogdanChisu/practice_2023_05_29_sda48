# import pymongo
# import datetime
# #pip install pymongo
# #este libraria de legatura intre baza de date mongodb si acest proiect python
#
# mongo_server = 'mongodb://localhost:27017'
# mongo_database = 'sda_48'
# mongo_collection = 'sda_48_col_1'
#
# client = pymongo.MongoClient(mongo_server)
# db_sda48 = client[mongo_database]
# collection = db_sda48[mongo_collection]
#
# #in mongodb se stockeaza "documente" (asa numesc) de tip json.
# #O alternativa de baze de date este SQL, acolo se lucreaza cu date de tip tabelar.
#
# doc_1 = {"nume":"Ionescu", "varsta": 49}
# collection.insert_one(doc_1)
#
# doc_2 = {"author": "Mike",
#         "text": "My first blog post!",
#         "tags": ["mongodb", "python", "pymongo"],
#         "date": datetime.datetime.utcnow()}
# collection.insert_one(doc_2)