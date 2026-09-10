from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/") 
print("Servidor:", client.admin.command("ping")) 
print("Bases:", client.list_database_names()) 
