import cv2
import face_recognition
import pickle
import os

# importing the student  images into a list
folderPath = r'E:\pradnya\Domains\Computer Vision\SmartAttendance\training_img'
PathList = os.listdir(folderPath)
print(PathList)
imgList = []
studentIds = []
for path in PathList:
    imgList.append(cv2.imread(os.path.join(folderPath,path)))
    print(path)
    # print(os.path.splitext(path)) # spliting path name, taking 0th path
    # print(os.path.splitext(path)[0])
    studentIds.append(os.path.splitext(path)[0])
print("len of img list",len(imgList))
print(studentIds)


def findEncodings(imageList):
#steps of encoding -- 1) change color
    encodelist =[]
    for img in imageList:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodelist.append(encode)
    return encodelist

print("encoding started")
encodeListKnown = findEncodings(imgList)
encodeListKnownwithId=[encodeListKnown,studentIds]
# print(encodeListKnown)
print("Encoding Complete")


# # now, we need to save this encodings and their id's to use it later. save it into a pickle file
file = open("EncodedfileNew.p","wb")
pickle.dump(encodeListKnownwithId,file)
file.close()
print("file saved")
