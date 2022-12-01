# this script will gather data from the road test on 11/23/22
from imuController import *
import csv
import time

def nextTest(trial):
    test = trial + 2
    if trial <= 2:
        next = input("Continue? [y/n]: ")
    else:
        next = "n"
    if next == "n" or trial > 2:
        #maybe put code here to send the file to me.
        return ["Complete"," "," "," "," "," "]
    else:
        print("running next trial")
        return ["Trial: " + str(test)," "," "," "," "," "]

controller = IMUController()
controller.start()
file = open('driftCalib1.csv','w')
writer = csv.writer(file)

writer.writerow(["Trial: 1"," "," "," "," "," "])

for i in range(4): # 4 trials will be recorded
    for j in range(500):
        data = [controller.Ax, controller.Ay, controller.Az, controller.Gx, controller.Gy, controller.Gz]
        writer.writerow(data)
        time.sleep(0.01)

    writer.writerow(nextTest(i))

file.close()
print("File closed.\nPlease exit.\n\n")
controller.end()
