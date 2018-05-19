#!/usr/bin/python3
try:
    import serial
except:
    print('Please install PySerial first')
    print('$pip install pyserial')
    exit()

import time
import random

serialPort = 'COM4' #serial where data is being sent from
timeToRun = 10 #minutes
sleepInterval = 30 #seconds between finishes

def randomTime(*args,**kwargs):
    """Generates a random time between 50.000 and 59.999 in bytes"""
    randomBytes = [
        128, #finish time indicator
        random.randrange(48,57), #thousandth
        random.randrange(48,57), #hundreth
        random.randrange(48,57), #tenth
        random.randrange(48,57), #seconds (first digit)
        53, #seconds (second digit)
        48, #seconds (third digit)
        13, #carriage return
        10, #newline
    ]
    return randomBytes

def main(*args,**kwargs):
    try:
        ser = serial.Serial(serialPort)
        endTime = int(time.time()) + (timeToRun * 60)
        while endTime > time.time():
            ser.write(randomTime())
            time.sleep(sleepInterval)
        ser.close()
    except:
        print('Error binding to specified serial', serialPort)
        exit()
    exit()

if __name__ == '__main__':
    main()
