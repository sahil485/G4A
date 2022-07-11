import pyfirmata
import time
from main import find_faces

board = pyfirmata.Arduino('COM3')

it = pyfirmata.util.Iterator(board)
it.start()

digital_input = board.get_pin('d:0:i')
motor_output = board.get_pin('d:1:o')

while True:
    button_state = digital_input.read()
    if button_state:

    else:
        continue
    time.sleep(0.1)