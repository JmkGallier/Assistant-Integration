#!/usr/bin/python3

import serial
import time
import os

ser = serial.Serial('/dev/ttyACM0', 9600, 8, 'N', 1, timeout=3)
RPI_project_id = "pi-pillbox-ca671"
RPI_model_id = "rasp-pillbox-46290"
bashcommand = "googlesamples-assistant-pushtotalk --project-id %s --device-model-id %s -i static_audio/date_query.raw" % (RPI_project_id, RPI_model_id)

pressed = False
while not pressed:
    my_str = ser.readline().decode("utf-8").replace("\r\n", "")
    if my_str == "Pressed":
        pressed = True
        break
    elif my_str == "Not Pressed":
        print("Calendar has been pressed")

os.system(bashcommand)
pressed = False
