import face_recognition
import pickle
import time
import cv2
import os

data = pickle.loads(open('face_enc', "rb").read())
# print(data)

video_capture = cv2.VideoCapture(0)
ret, image = video_capture.read()

faces = face_recognition.face_locations(image, model='hog')

# cascPathface = os.path.dirname(
#  cv2.__file__) + "/data/haarcascade_frontalface_default.xml"
# faceCascade = cv2.CascadeClassifier(cascPathface)
# faces = faceCascade.detectMultiScale(image,
#                                          scaleFactor=1.1,
#                                          minNeighbors=5,
#                                          minSize=(200, 200),
#                                          flags=cv2.CASCADE_SCALE_IMAGE)

encodings = face_recognition.face_encodings(image)
names = []

for encoding in encodings:
    matches = face_recognition.compare_faces(data['encodings'], encoding)
    name = "Unknown"

    if True in matches:
        matchedIdxs = [i for (i, b) in enumerate(matches) if b]
        print(matchedIdxs)
        counts = {}
        # loop over the matched indexes and maintain a count for
        # each recognized face face
        for i in matchedIdxs:
            #Check the names at respective indexes we stored in matchedIdxs
            name = data["names"][i]
            #increase count for the name we got
            counts[name] = counts.get(name, 0) + 1
            #set name which has highest count
        name = max(counts, key=counts.get)

        names.append(name)

for ((y1, x2, y2, x1), name) in zip(faces, names):
    # rescale the face coordinates
    # draw the predicted face name on the image
    cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
    cv2.putText(image, name, (x1, y1), cv2.FONT_HERSHEY_SIMPLEX,
        0.75, (0, 255, 0), 2)

cv2.imshow("Frame", image)
cv2.waitKey(0)