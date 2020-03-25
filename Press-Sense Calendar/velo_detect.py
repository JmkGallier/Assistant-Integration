#!/usr/bin/python3

import serial
import time
import os

ser = serial.Serial('/dev/ttyACM0', 9600, 8, 'N', 1, timeout=3)
pressed = False

bashcommand = "googlesamples-assistant-pushtotalk --project-id pi-pillbox-ca671 --device-model-id rasp-pillbox-46290 -i static_audio/date_query.raw"


while not pressed:
    my_str = ser.readline().decode("utf-8").replace("\r\n", "")
    if my_str == "PUSH":
        pressed = True
        break
    elif my_str == "NOT PUSH":
        print("This aint the one chief")

os.system(bashcommand)
pressed = False
