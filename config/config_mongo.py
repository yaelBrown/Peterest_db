from pymongo import MongoClient

client = MongoClient("mongodb+srv://pet_owner:pets@peterest-db.fkffd.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.get_database('Peterest_db')