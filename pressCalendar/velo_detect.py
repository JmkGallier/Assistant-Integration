#!/usr/bin/python3

# import serial
# import time
import os


RPI_project_id = "pi-pillbox-ca671"
RPI_model_id = "rasp-pillbox-46290"
date_query_location = "static_audio/date_query.raw"

# Declares absolute path
pressSense_dir = os.path.dirname(os.path.realpath(__file__))
repo_dir = os.path.dirname(pressSense_dir)
AsstIntegration_script_dir = os.path.join(pressSense_dir + "/AsstIntegration")
date_query_location = os.path.join(pressSense_dir, date_query_location).replace(" ", "\\ ")
bash_prefix = "/bin/bash "
expect_prefix = "/usr/bin/expect"

bash_Assistant = "%s %s/GA_calendar_trigger.exp %s" % (expect_prefix, pressSense_dir, repo_dir)


os.system(bash_Assistant)

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
