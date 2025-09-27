from pymongo.mongo_client import MongoClient
from urllib.parse import quote_plus

# Properly escape the username and password
username = quote_plus("Tara")
password = quote_plus("Tara@1234")
uri = f"mongodb+srv://{username}:{password}@cluster0.3gsaj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
# try:
# client.admin.command('ping')
# print("Pinged your deployment. You successfully connected to MongoDB!")

# # Access the database and collection
# db = client['Smart_Attendance']  # Replace with your database name
# collection = db['TY-C']  # Replace with your collection name

# # Data to be inserted
# data = {
#     "2223000132": {
#         "name": "Shantanu Mahadik",
#         "total_attendance": 75,
#     },
#     "2223000139": {
#         "name": "Pradnya Mahadik",
#         "total_attendance": 75,
#     },
#     "2223000872": {
#         "name": "Utkarsha Kavathekar",
#         "total_attendance": 75,
#     },
#     "2223000185": {
#         "name": "Sakshi Nakate",
#         "total_attendance": 75,
#     },
#     "2223000383": {
#         "name": "Chahat Pathan",
#         "total_attendance": 75,
#     },
#     "2223000870": {
#         "name": "Sayli Patil",
#         "total_attendance": 75,
#     }
# }

# # Insert data into the collection
# # Insert the data into MongoDB
# # Insert the data into MongoDB with upsert
# for student_id, student_info in data.items():
#     collection.update_one(
#         {"_id": student_id},      # Use student_id directly
#         {"$set": student_info},   # Update the document with student_info
#         upsert=True               # Insert if it does not exist
#     )

# print("Data inserted/updated successfully!")


# except Exception as e:
#     print(e)
# finally:
#     # Close the connection
#     client.close()
#     print("Connection closed.")

# ////////////////////////////////////////////////////////////////////////////////////////////////////
# add entries in database:
# To insert a single document, use db.collection.insertOne().
# To insert multiple documents, use db.collection.insertMany().

# Correct way to add multiple entries
# new_entries = [
#     {
#         "_id": "2223000392",
#         "name": "Omkar Kore",
#         "total_attendance": 75,
#     },
#     {
#         "_id": "2223000102",
#         "name": "Abhay Patil",
#         "total_attendance": 76,
#     }
# ]

# # Insert multiple documents into the collection
# collection.insert_many(new_entries)
# print("new entries entered successfully")

# collection.insert_one({
#         "_id": "2223000149",
#         "name": "Kalyani Patil",
#         "total_attendance": 76,
#     })
# print("new entries entered successfully")



# Access the database and collection
db = client['Smart_Attendance']  # Replace with your database name
collection = db['attendance_2024-11-22']  # Replace with your collection name

# # Data to be inserted

data = {
   "2223000132":{
  "time": "00:00:00",
  "status": "Absent"  },

   "2223000139":{
  "time": "00:00:00",
  "status": "Absent"  },

   "2223000872":{
  "time": "00:00:00",
  "status": "Absent"  },

   "2223000185":{
  "time": "00:00:00",
  "status": "Absent"  },

   "2223000383":{
  "time": "00:00:00",
  "status": "Absent"  },

   "2223000870":{
  "time": "00:00:00",
  "status": "Absent"  },

   "2223000392":{
  "time": "00:00:00",
  "status": "Absent"  },

   "2223000102":{
  "time": "00:00:00",
  "status": "Absent"  },

   "2223000149":{
  "time": "00:00:00",
  "status": "Absent"  },
}
for student_id, student_info in data.items():
    collection.update_one(
        {"_id": student_id},      # Use student_id directly
        {"$set": student_info},   # Update the document with student_info
        upsert=True               # Insert if it does not exist
    )
print("Data inserted successfully")
  
   

# client.close()
# print("Connection closed.")
# Delete IP: 0.0.0.0/0