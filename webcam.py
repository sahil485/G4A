import face_recognition
import pickle
import time
import cv2
import os
 
#find path of xml file containing haarcascade file 
cascPathface = os.path.dirname(
 cv2.__file__) + "/data/haarcascade_frontalface_default.xml"
# load the harcaascade in the cascade classifier
faceCascade = cv2.CascadeClassifier(cascPathface)
# load the known faces and embeddings saved in last file
data = pickle.loads(open('face_enc', "rb").read())

video_capture = cv2.VideoCapture(0)
while True:
    # grab the frame from the threaded video stream
    ret, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(frame,
                                         scaleFactor=1.1,
                                         minNeighbors=5,
                                         minSize=(50, 50),
                                         flags=cv2.CASCADE_SCALE_IMAGE)

    print(faces)

    encodings = face_recognition.face_encodings(frame)
    names = []

    for encoding in encodings:
       #Compare encodings with encodings in data["encodings"]
       #Matches contain array with boolean values and True for the embeddings it matches closely
       #and False for rest
        matches = face_recognition.compare_faces(data["encodings"],
         encoding)
        #set name =inknown if no encoding matches
        name = "Unknown"
        # check to see if we have found a match
        if True in matches:
            #Find positions at which we get True and store them
            matchedIdxs = [i for (i, b) in enumerate(matches) if b]
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

    for (face, name) in zip(faces, names):
        # rescale the face coordinates
        # draw the predicted face name on the image
        frame = cv2.rectangle(frame, face, color=(0, 255, 0), thickness=2)
        cv2.putText(frame, name, (face[-1], face[0]), cv2.FONT_HERSHEY_SIMPLEX,
            0.75, (0, 255, 0), 2)
 
    # convert the input frame from BGR to RGB 

    for face in faces:
        frame = cv2.rectangle(frame, face, color=(0, 255, 0), thickness=2)

    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()