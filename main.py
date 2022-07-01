import face_recognition
import pickle
import cv2
import os

# imagePaths = list(paths.list_images('Images'))
imageDir = 'images'
imagePaths = os.listdir(imageDir)

knownEncodings = []
knownNames = []

for (i, imageName) in enumerate(imagePaths):
    name = imageName.split('.')[0]
    image = cv2.imread(os.path.join(imageDir, imageName))
    print(image.shape)
    # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (200, 200))
    # print(image.shape)

    cv2.imshow('img', image)
    # cv2.waitKey(5000)

    boxes = face_recognition.face_locations(image, model='cnn')
    print("Boxes:", boxes)

    for box in boxes:
        y1, x2, y2, x1 = box
        image = cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
        print("here")
    
    cv2.imshow('image', image)
    cv2.waitKey(0)
    cv2.destroyWindow("img")
    cv2.destroyWindow("image")
    
    encodings = face_recognition.face_encodings(image, boxes)
    print("Encodings:", encodings)

    for encoding in encodings:  
        knownEncodings.append(encoding)
        knownNames.append(name)

data = {"encodings": knownEncodings, "names": knownNames}

print(data)
