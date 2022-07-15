import pyfirmata
import time
from main import find_faces

board = pyfirmata.Arduino('COM3')
print("Communication Successfully started")

it = pyfirmata.util.Iterator(board)
it.start()

digital_input = board.get_pin('d:4:i')
led = board.get_pin('d:13:o')

button_press_time = time.time()

while True:
    sw = digital_input.read()
    if sw is True and time.time() - button_press_time > 5:
        print("Finding faces...")
        people = find_faces()
        print("Found {}".format(people))
        button_press_time = time.time()
        led.write(1)
    else:
        led.write(0)
    time.sleep(0.1)