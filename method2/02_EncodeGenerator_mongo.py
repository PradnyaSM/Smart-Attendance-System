# import cv2
# import face_recognition
# import os
# import numpy as np
# from pymongo.mongo_client import MongoClient

# # Connect to MongoDB Atlas

# from pymongo.mongo_client import MongoClient
# from urllib.parse import quote_plus

# # Properly escape the username and password
# username = quote_plus("Tara")
# password = quote_plus("Tara@1234")
# uri = f"mongodb+srv://{username}:{password}@cluster0.3gsaj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# # Create a new client and connect to the server
# client = MongoClient(uri)
# db = client['Smart_Attendance']  # Replace with your database name

# students_collection = db["students"]

# # Path to the folder containing student images
# folderPath = r'E:\pradnya\Domains\Computer Vision\SmartAttendance\training_img'

# # Initialize lists to store student IDs and their encodings
# studentIds = []
# encodeListKnown = []

# # List of all image file names in the folder
# PathList = os.listdir(folderPath)

# for path in PathList:
#     # Load each image
#     img = cv2.imread(os.path.join(folderPath, path))
    
#     # Convert the image to RGB (face_recognition requires RGB format)
#     img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
#     # Get the face encoding (assuming one face per image)
#     encodings = face_recognition.face_encodings(img_rgb)
    
#     if encodings:
#         # Take the first encoding (for single face images)
#         encode = encodings[0]
        
#         # Extract student ID from filename (e.g., "student123.jpg" -> "student123")
#         student_id = os.path.splitext(path)[0]
        
#         # Append data to lists
#         studentIds.append(student_id)
#         encodeListKnown.append(encode)

# print("Encoding completed for all images.")

# # Insert each student's encoding into MongoDB
# for student_id, encoding in zip(studentIds, encodeListKnown):
#     student_data = {
#         "student_id": student_id,
#         "name": student_id,  # Replace with actual names if available
#         "encoding": encoding.tolist()  # Convert encoding from numpy array to list
#     }
#     students_collection.insert_one(student_data)

# print("Student encodings inserted into MongoDB")


# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# uploading images
import cv2
import face_recognition
import os
import numpy as np
from pymongo import MongoClient
import gridfs




from pymongo.mongo_client import MongoClient
from urllib.parse import quote_plus

# # Properly escape the username and password
username = quote_plus("Tara")
password = quote_plus("Tara@1234")
uri = f"mongodb+srv://{username}:{password}@cluster0.3gsaj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# # Create a new client and connect to the server
client = MongoClient(uri)
db = client['Smart_Attendance']  # Replace with your database name

students_collection = db["Photos"]
fs = gridfs.GridFS(db)

folderPath = r'E:\pradnya\Domains\Computer Vision\SmartAttendance\training_img'
PathList = os.listdir(folderPath)

for path in PathList:
    img_path = os.path.join(folderPath, path)
    img = cv2.imread(img_path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    encodings = face_recognition.face_encodings(img_rgb)
    if encodings:
        encode = encodings[0]
        student_id = os.path.splitext(path)[0]
        
        # Upload image to GridFS
        with open(img_path, "rb") as image_file:
            gridfs_id = fs.put(image_file, filename=path)

        student_data = {
            "student_id": student_id,
            "encoding": encode.tolist(),
            "image_gridfs_id": gridfs_id  # Reference to the image in GridFS
        }
        students_collection.insert_one(student_data)

print("Student encodings and images (via GridFS) inserted into MongoDB")

