#!/usr/bin/python3
import serial
import time
import os
import struct
# import RPi.GPIO as GPIO    # Can only be run on a RPi


def ardOutput_tuple():
    try:
        ard_tuple = ser.readline().decode("utf-8").replace("\r\n", "").split(" ")
        soil_level = float(ard_tuple[0])
        dist_level = float(ard_tuple[1])
        print("M: %g | Prox: %g\n" % (soil_level, dist_level))
        return soil_level, dist_level
    except ValueError:
        time.sleep(5000)
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
        os.system(bash_thirsty)
        check_attempt += 1
        ser.reset_input_buffer()
        water_check = ardOutput_tuple()
        print(check_attempt, water_check)
        
        if water_check[0] < soil_threshold:
            ser.write(struct.pack(">B", soil_threshold))
            time.sleep(5)
        else:
            os.system(bash_satis)
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

# 
ser = serial.Serial('/dev/ttyS0', 9600, 8, 'N', 1, timeout=7)
audio_prefix = "".join(["aplay --format=S16_LE --rate=16000 ", os.getcwd()]).replace("t ", "t\\ ")
bash_thirsty = audio_prefix + "/static_audio/thirsty.raw"
bash_satis = audio_prefix + "/static_audio/satisfied_plant.raw"
bash_watered = audio_prefix + "/static_audio/watered_plant.raw"

# Sensor Thresholds
dist_threshold = 0
soil_threshold = 40


def dev():
    dev_counter = 0
    while dev_counter < 50:
        try:
            dev_counter += 1
            ard_tuple = ser.readline().decode("utf-8").replace("\r\n", "")#.split(" ")
            print(ard_tuple)
        except IndexError:
            continue

#dev()
driver()
