from pymongo.mongo_client import MongoClient
from urllib.parse import quote_plus

# Escape username and password
username = quote_plus("Pradnya")
password = quote_plus("Rose@1234")
uri = f"mongodb+srv://{username}:{password}@cluster0.comlw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

from datetime import datetime

# MongoDB connection (replace with your MongoDB Atlas URI)
db = client['attendance_system']  # Use or create the database
collection = db['students_TY_C']  # Use or create the collection

# Data to be inserted
data = [
    {
        # "_id": "2223000132",
        "name": "Shantanu Mahadik",
        "total_attendance": 75,
        "last_attendance_time": datetime.strptime("2022-12-11 00:54:34", "%Y-%m-%d %H:%M:%S")
    },
    {
        "_id": "2223000139",
        "name": "Pradnya Mahadik",
        "total_attendance": 75,
        "last_attendance_time": datetime.strptime("2022-12-11 00:54:34", "%Y-%m-%d %H:%M:%S")
    },
    {
        "_id": "2223000536",
        "name": "Atharva Rane",
        "total_attendance": 75,
        "last_attendance_time": datetime.strptime("2022-12-11 00:54:34", "%Y-%m-%d %H:%M:%S")
    },
    {
        "_id": "2223000184",
        "name": "Sakshi Nakate",
        "total_attendance": 75,
        "last_attendance_time": datetime.strptime("2022-12-11 00:54:34", "%Y-%m-%d %H:%M:%S")
    },
    {
        "_id": "2223000872",
        "name": "Utkarsha Kavathekar",
        "total_attendance": 75,
        "last_attendance_time": datetime.strptime("2022-12-11 00:54:34", "%Y-%m-%d %H:%M:%S")
    },
    {
        "_id": "2223000880",
        "name": "Sayli Patil",
        "total_attendance": 75,
        "last_attendance_time": datetime.strptime("2022-12-11 00:54:34", "%Y-%m-%d %H:%M:%S")
    },
    
]

# Insert the data into MongoDB
# Insert the data into MongoDB with upsert
for student in data:
    collection.update_one(
        {"_id": student["_id"]},  # Filter by _id
        {"$set": student},        # Update the document
        upsert=True               # Insert if it does not exist
    )
print("Data inserted/updated successfully!")

