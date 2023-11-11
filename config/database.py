from pymongo import MongoClient
import urllib

client = MongoClient("mongodb+srv://admin:admin." + urllib.parse.quote("123123@") + "@cluster0.7pbr4.mongodb.net/?retryWrites=true&w=majority")

db = client.db_example_temp

colection_name = db["agents"]

