import face_recognition
import pickle
import cv2
import os

imageDir = 'images'
imagePaths = os.listdir(imageDir)

knownEncodings = []
knownNames = []

for (i, imageName) in enumerate(imagePaths):
    print(imageName)
    name = imageName.split('.')[0].split('-')[0]
    image = cv2.imread(os.path.join(imageDir, imageName))
    # image = cv2.resize(image, (224, 224))

    boxes = face_recognition.face_locations(image, model='cnn')
    # print("Boxes:", boxes)

    encodings = face_recognition.face_encodings(image, boxes)
    # print("Encodings:", encodings)

    # for encoding in encodings:  
    #     knownEncodings.append(encoding)
    #     knownNames.append(name)

    assert len(boxes) == len(encodings)
    print("[INFO] Name: {} Number of Boxes: {} Number of Encodings: {}".format(imageName.split('.')[0], len(boxes), len(encodings)))
    
    # Add first encoding (probably for biggest face)
    knownEncodings.append(encodings[0])
    knownNames.append(name)
    
    for box in boxes:
        y1, x2, y2, x1 = box
        image = cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
    
    # cv2.imshow('image', image)
    # cv2.waitKey(0)

data = {"encodings": knownEncodings, "names": knownNames}

f = open("face_enc", "wb")
f.write(pickle.dumps(data))
f.close()