#!/usr/bin/python3

# import serial
# import time
import os


RPI_project_id = "pi-pillbox-ca671"
RPI_model_id = "rasp-pillbox-46290"
date_query_location = "static_audio/date_query.raw"

# Declares absolute path
script_directory = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(script_directory)
AsstIntegration_Dir = os.path.dirname(script_directory + "/AsstIntegration")
date_query_location = os.path.join(script_directory, date_query_location).replace(" ", "\\ ")

bash_Assistant = "googlesamples-assistant-pushtotalk --project-id %s --device-model-id %s -i %s" % (RPI_project_id,
                                                                                                 RPI_model_id,
                                                                                                 date_query_location)
bash_start_virtmic = ".%s -s virtmic_start" % AsstIntegration_Dir
bash_play_virtmic = ".%s -s virtmic_play" % AsstIntegration_Dir

#os.system(bashcommand)
print(date_query_location)

# ser = serial.Serial('/dev/ttyACM0', 9600, 8, 'N', 1, timeout=3)
# pressed = False
# while not pressed:
#     my_str = ser.readline().decode("utf-8").replace("\r\n", "")
#     if my_str == "Pressed":
#         pressed = True
#         break
#     elif my_str == "Not Pressed":
#         print("Calendar has been pressed")
# pressed = False
