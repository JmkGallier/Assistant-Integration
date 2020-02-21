import RPi.GPIO as GPIO
import time
import os


test_input = 1
bashcommand = "googlesamples-assistant-pushtotalk --project-id pi-pillbox-ca671 --device-model-id rasp-pillbox-46290 -i date_query.raw"

pin_set = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_set, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(pin_set)
    if input_state == False:
        os.system(bashcommand)
        time.sleep(0.2)


