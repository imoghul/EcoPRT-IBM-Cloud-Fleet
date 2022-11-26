import io
import pynmea2
import serial
import time
import sys
import os

try:
    ser = serial.Serial(port='/dev/ttyACM0',timeout=1)
    sio = io.TextIOWrapper(io.BufferedRWPair(ser,ser))
except:
    ser = None
    sio = None


def getGPSData():
    try:
        line = sio.readline()
        msg = pynmea2.parse(line)
        #print(msg)
        if type(msg) == pynmea2.types.talker.RMC:

            status = msg.status

            if status == 'A':

                zeit = msg.datetime

                latitude = msg.latitude
                longitude = msg.longitude
                return(zeit, latitude,longitude)

    except serial.SerialException as e:
        print(str(e))#pass
    except pynmea2.ParseError as e:
        print(str(e))#raise e
    except UnicodeDecodeError as e:
        print(str(e))#raise e
    except:
        pass
    return (None,None,None)
