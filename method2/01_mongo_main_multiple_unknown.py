import os
import pickle
import cv2
import face_recognition
import numpy as np
from datetime import datetime

# MongoDB connection setup
from pymongo.mongo_client import MongoClient
from urllib.parse import quote_plus

# Properly escape the username and password
username = quote_plus("Tara")
password = quote_plus("Tara@1234")
uri = f"mongodb+srv://{username}:{password}@cluster0.3gsaj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)
db = client["Smart_Attendance"]
attendance_collection = db["attendance_records:"]

print("Start")
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(3, 640)
cap.set(4, 480)

# Load encoded file
print("Loading encoded files")
file = open('EncodedfileNew.p', 'rb')
encodeListKnownwithId = pickle.load(file)
file.close()
encodeListKnown, studentIds = encodeListKnownwithId
print("Loaded encoded files")

id = str(-1)
counter = 0

# Initialize a set to keep track of processed IDs
processed_ids = set()
while True:
    success, img = cap.read()
    imgSmall = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgSmall = cv2.cvtColor(imgSmall, cv2.COLOR_BGR2RGB)

    faceCurrntFrame = face_recognition.face_locations(imgSmall)
    encodeCurrentFrame = face_recognition.face_encodings(imgSmall, faceCurrntFrame)

    for encodeface, faceloc in zip(encodeCurrentFrame, faceCurrntFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeface)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeface)
        matchIndex = np.argmin(faceDis)
        print("matchindex:",matchIndex)

        if matches[matchIndex]:
            print("Known face detected")
            print(studentIds[matchIndex])
            id = str(studentIds[matchIndex])
            if id not in processed_ids:  # Check if ID has already been processed
                processed_ids.add(id)  # Add ID to the processed set

            if counter == 0:
                counter = 1
            print("counter is",counter)
# change
        else:
            # Handle unknown face
            id = "Unknown Face"  # Set ID to indicate unknown face
            print("Unknown face detected")

        # draw rectangle
        top, right, bottom, left = faceloc

        # Scale the face location coordinates back to the original image size
        height, width, _ = img.shape
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 2)

        # Display the ID of the detected face below the rectangle
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, id, (left, bottom + 20), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)
        
    if counter != 0:
        if counter == 1:
            print("Entered counter loop")
            # Retrieve student information from MongoDB
            studentInfo = attendance_collection.find_one({"_id": id})
            print(studentInfo)

            if studentInfo:
                # Check last attendance time
                datetimeObject = datetime.strptime(studentInfo['time'], "%H:%M:%S")
                secondsElapsed = (datetime.now() - datetimeObject).total_seconds()
                print("Seconds elapsed:", secondsElapsed)

                # Update attendance if more than 30 seconds have passed
                if secondsElapsed > 30:
                    # Update student status to "present" and update time
                    attendance_collection.update_one(
                        {"_id": id},
                        {"$set": {
                            "status": "present",
                            "time": datetime.now().strftime("%H:%M:%S")
                        }}
                    )
                    print(f"Attendance marked for {id}")
                    counter = 0  # Reset counter after marking attendance
                else:
                    print("Already marked")
            else:
                print("No student information found.")

        # Increment counter to prevent immediate re-check only if studentInfo exists
        counter += 1


    if counter > 30:
        counter = 0

    
    # Reset processed IDs after each frame
    processed_ids.clear()    

    cv2.imshow("Face Attendance", img)
    k = cv2.waitKey(33) & 0xFF
    if k == ord('s'):
        break

cap.release()
cv2.destroyAllWindows()


# client.close()
# print("closed")