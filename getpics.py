import cv2
import time

stream = cv2.VideoCapture(0)
while True:
    name = input("Enter name: ")
    for i in range(30):
        ret, frame = stream.read()
        cv2.imwrite('images/{}-{}.jpg'.format(name, i), frame)
        cv2.imshow('{} image {}'.format(name, i), frame)
        cv2.waitKey(0)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
stream.release()

    