import io
import pynmea2
import serial
import time
import logging
import sys
import os


ser = serial.Serial(port='/dev/ttyACM0',timeout=1)
sio = io.TextIOWrapper(io.BufferedRWPair(ser,ser))



def getGPSData():
    try:
        line = sio.readline()
        msg = pynmea2.parse(line)
        #print(msg)
        if type(msg) == pynmea2.types.talker.RMC:

            status = msg.status

            if status == 'A':
                logger.debug('Got Fix')

                zeit = msg.datetime

                latitude = msg.latitude
                longitude = msg.longitude
                return(zeit, latitude,longitude)

    except serial.SerialException as e:
        pass
    except pynmea2.ParseError as e:
        raise e
    except UnicodeDecodeError as e:
        raise e
    return (0,0,0)
