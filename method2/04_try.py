from pymongo.mongo_client import MongoClient
from urllib.parse import quote_plus
import gridfs
import os

# Properly escape the username and password
username = quote_plus("Tara")
password = quote_plus("Tara@1234")
uri = f"mongodb+srv://{username}:{password}@cluster0.3gsaj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)
db = client['Smart_Attendance']  # Replace with your database name
collection = db['TY-C'] 
client.close()
print("closed")

db = client['Smart_Attendance']  # Replace with your database name
collection = db['Photos'] 
client.close()
print("closed")

db = client['Smart_Attendance']  # Replace with your database name
collection = db['students'] 
client.close()
print("closed")