import pyfirmata
import time
from main import *
import pandas as pd
from datetime import datetime

board = pyfirmata.Arduino('COM3')
print("Communication Successfully started")

it = pyfirmata.util.Iterator(board)
it.start()

digital_input = board.get_pin('d:4:i')

motor1_pin1 = board.get_pin('d:2:o')
motor1_pin2 = board.get_pin('d:3:o')

button_press_time = time.time()

def run_motor():
    global motor1_pin1, motor1_pin2
    # print("Running motor...")
    motor1_pin1.write(1)
    motor1_pin2.write(0)
    time.sleep(1)
    motor1_pin1.write(0)
    motor1_pin2.write(0)

df = pd.read_csv('gumballs.csv')
df["Time"] = pd.to_datetime(df['Time'])
wait_time = 30

while True:
    button_state = digital_input.read()
    if button_state and time.time() - button_press_time > 5:
        people = find_faces()
        print("Finding faces...")
        # print("Found {}".format(people))
        button_press_time = time.time()
    else:
        continue

    if people:
        for person in people:
            # print(person in df['Name'].unique())
            if person in df['Name'].unique() and (datetime.now() - df.loc[df.Name == person, "Time"].item()).total_seconds() > wait_time:
                print("Found {}".format(person))
                run_motor()
                time.sleep(1)
                df.loc[df.Name == person, "Time"] = datetime.now()
                # print(df)
                if person in df["Name"].unique():
                    print("{} has been updated in the gumball database!".format(person), end=" ")    
                else:
                    print("{} has been added to the gumball database!".format(person), end=" ")
                print("Enjoy {}!".format(person))
            elif person not in df["Name"].unique():
                run_motor()
                df.loc[len(df.index)] = [person, datetime.now()]
                # print(df)
                print("{} has been added to the gumball database. Enjoy {}!".format(person, person))
                time.sleep(1)
            else:
                print("{} has already gotten a gumball. They must wait another {:.2f} second(s)".format(person, wait_time - (datetime.now() - df[df["Name"] == person]["Time"].item()).total_seconds()))
                # print(df)
                time.sleep(1)
                
            df.to_csv('gumballs.csv', index=False)

    else:
        print("No people were found! Stop hiding!")
        time.sleep(1)

    time.sleep(0.1)