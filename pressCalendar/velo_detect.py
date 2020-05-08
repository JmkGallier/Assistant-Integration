#!/usr/bin/python3

# import serial
# import time
import os
# 
# ser = serial.Serial('/dev/ttyACM0', 9600, 8, 'N', 1, timeout=3)
pwd = os.getcwd()
RPI_project_id = "pi-pillbox-ca671"
RPI_model_id = "rasp-pillbox-46290"

# Declares absolute path
script_directory = os.path.dirname(os.path.realpath(__file__))
audiofile_loc = os.path.join(script_directory, "date_query.raw").replace(" ", "\\ ")

#command2 = os.path.join(script_directory, "!!!!!!!!!!!").replace(" ", "\\ ")

bashcommand = "googlesamples-assistant-pushtotalk --project-id %s --device-model-id %s -i %s" % (RPI_project_id, RPI_model_id, audiofile_loc)

# pressed = False
# while not pressed:
#     my_str = ser.readline().decode("utf-8").replace("\r\n", "")
#     if my_str == "Pressed":
#         pressed = True
#         break
#     elif my_str == "Not Pressed":
#         print("Calendar has been pressed")

# pressed = False
os.system(bashcommand)
#print(audiofile_loc)
