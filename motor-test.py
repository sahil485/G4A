import pyfirmata
import time

board = pyfirmata.Arduino('COM3')
print("Communication Successfully started")

motor1pin1 = board.get_pin('d:2:o')
motor1pin2 = board.get_pin('d:3:o')

motor1pin1.write(1)
motor1pin2.write(0)
time.sleep(1)
motor1pin1.write(0)
motor1pin2.write(0)
print("Communication Successfully ended")
# while True:
#     board.digital[3].write(1)
#     time.sleep(1)
#     board.digital[3].write(0)
#     time.sleep(1)