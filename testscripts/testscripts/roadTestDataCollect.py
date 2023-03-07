# this script will gather data from the road test on 11/23/22
# Updating script for ML Model data collection on 3/3/2023
from imuController import *
import csv
import time
import signal
import sys

def nextTest(trial):
    test = trial + 2
    if trial <= 2:
        next = input("Continue? [y/n]: ")
    else:
        next = "n"
    if next == "n" or trial > 2:
        # maybe put code here to send the file to me.
        return ["Complete"," "," "," "," "," "," "]
    else:
        print("running next trial")
        return ["Trial: " + str(test)," "," "," "," "," "," "]
    
def sigint_handler(signal, frame):
    print('\nReceived CTRL + C, pausing collection.')

    proceed = False

    while not proceed:
        command = input("Resume collection? (y/n): ")
        if command == "y":
            proceed = True
            print("Continuing Data collection")
        elif command == "n":
            print("Exiting.")
            file.close()
            sys.exit(0)


controller = IMUController()
controller.start()
file = open('ml_data_collect.csv','w')
writer = csv.writer(file)

# allows our program to detect if a SIGINT signal has been received
signal.signal(signal.SIGINT, sigint_handler)

writer.writerow(["Beginning Data Collection"," "," "," "," "," "," "])

# keeps track of time elapsed
orig_time = time.time()

while True:
    data = [controller.Ax, controller.Ay, controller.Az, controller.Gx, controller.Gy, controller.Gz, time.time()]
    writer.writerow(data)

    time_elapsed = time.time() - orig_time

    if time_elapsed >= 1.99 and time_elapsed <= 2.01:
        print("Current time: " + str(time.time()))
        orig_time = time.time()

    time.sleep(0.0333333333)

# for i in range(trials): # records as many trials as the user entered
#
#     for j in range(milliseconds):
#         data = [controller.Ax, controller.Ay, controller.Az, controller.Gx, controller.Gy, controller.Gz, time.time()]
#         writer.writerow(data)
#         time.sleep(0.01)
#
#     writer.writerow(nextTest(i))

file.close()
print("File closed.\nPlease exit.\n\n")
controller.end()
