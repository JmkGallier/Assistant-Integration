#!/usr/bin/python3
import serial
import time
import os
import struct
# import RPi.GPIO as GPIO    # Can only be run on a RPi


def ardOutput_tuple():
    try:
        #ser.write(struct.pack(">B", soil_threshold)) # Request sensor data from Ard
        ser.reset_input_buffer()
        ard_tuple = ser.readline().decode("utf-8").replace("\r\n", "").split(" ")
        soil_level = float(ard_tuple[0])
        dist_level = float(ard_tuple[1])
        print("M: %g | Prox: %g\n" % (soil_level, dist_level))
        return soil_level, dist_level
    except ValueError:
        time.sleep(1000)
        return ardOutput_tuple()


def soilCheck(rasp_input):
    soil_level = rasp_input[0]
    soilCheck_out = 0
    if soil_level <= soil_threshold:
        soilCheck_out = 1
    return soilCheck_out


def distCheck(rasp_input):
    dist_level = rasp_input[1]
    distCheck_out = 0
    if dist_level:
        print("User in Proximity")
        distCheck_out = 1
    return distCheck_out


def userCheck():
    check_attempt = 0
    while check_attempt < 3:
        check_attempt += 1
        water_check = ardOutput_tuple()
        print(check_attempt, water_check)
        
        if water_check[0] < soil_threshold:
            os.system(bash_thirsty)
            time.sleep(5)
        else:
            os.system(bash_watered)
            check_attempt = 3


def main():
    pass
        

def driver():
    dev_counter = 0
    while dev_counter < 50:
        try:
            ard_out = ardOutput_tuple()
            soil_status = soilCheck(ard_out)
            
            dev_counter += 1
            if soil_status:
                dist_status = distCheck(ard_out)
                if dist_status:
                    userCheck()
                else:
                    pass
        except IndexError:
            continue

# # Can only be run on RPi
# # GPIO Config 
# GPIO_LED_red = 24
# GPIO_LED_green = 23
# GPIO.setwarnings(False)
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(GPIO_LED_red, GPIO.OUT)
# GPIO.setup(GPIO_LED_green, GPIO.OUT)


# Serial Connection
ser = serial.Serial('/dev/ttyS0', 9600, 8, 'N', 1, timeout=7)

#
audio_prefix = "aplay --format=S16_LE --rate=16000 "
script_directory = os.path.dirname(os.path.realpath(__file__))
bash_thirsty = os.path.join(script_directory, "static_audio/thirsty.raw").replace(" ", "\\ ")
bash_satis = os.path.join(script_directory, "static_audio/satisfied_plant.raw").replace(" ", "\\ ")
bash_watered = os.path.join(script_directory, "static_audio/watered_plant.raw").replace(" ", "\\ ")
bash_thirsty = (audio_prefix + bash_thirsty)
bash_satis = (audio_prefix + bash_satis)
bash_watered = (audio_prefix + bash_watered)

# Sensor Thresholds
dist_threshold = 0
soil_threshold = 40


driver()
