import cv2

v = cv2.VideoCapture(0)
ret, image = v.read()
print(image)