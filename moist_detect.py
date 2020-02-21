#!/usr/bin/python3

import serial
import time
import os

ser = serial.Serial('/dev/ttyACM0', 9600, 8, 'N', 1, timeout=3)
pressed = False

bashcommand = "aplay --format=S16_LE --rate=16000 watered_plant.raw"

while not pressed:
    my_str = ser.readline().decode("utf-8").replace("\r\n", "")
    ser_param = my_str.split(" ")
    moist_par = ser_param[0]
    if moist_par == "high":
        pressed = True
        break
    elif moist_par == "low":
        print("This aint the one chief")

os.system(bashcommand)
pressed = False
