#!/usr/bin/python3
import serial
import time
import os
import RPi.GPIO as GPIO


def ardOutput_tuple():
    ard_tuple = ser.readline().decode("utf-8").replace("\r\n", "").split(" ")
    soil_level = float(ard_tuple[0])
    dist_level = float(ard_tuple[1])
    return soil_level, dist_level


def soilCheck(rasp_input):
    soil_level = rasp_input[0]
    soilCheck_out = 0
    if soil_level > soil_threshold:
        print("Soil Greater than Threshold")
        soilCheck_out = 0
    elif soil_level <= soil_threshold:
        print("Soil Less than Threshold")
        soilCheck_out = 1
    return soilCheck_out


def distCheck(rasp_input):
    dist_level = rasp_input[1]
    distCheck_out = 0
    if dist_level > dist_threshold:
        print("User is Not in Proximity")
        distCheck_out = 0
    elif dist_level <= dist_threshold:
        print("User in Proximity")
        distCheck_out = 1
    return distCheck_out


def userCheck():
    pass


def main():
    pass


def driver():
    dev_counter = 0
    while dev_counter < 50:
        try:
            ard_out = ardOutput_tuple()
            soil_status = soilCheck(ard_out)
            
            if soil_status == 0:
                continue
            elif soil_status == 1:
                dist_status = distCheck(ard_out)
                if dist_status == 0:
                    continue
                elif dist_status == 1:
                    
                    
            
            print("Iteration: %d | Soil: %g | Distance: %g" % (dev_counter+1, ard_out[0], ard_out[1]))
            dev_counter += 1
        except IndexError:
            continue


# GPIO Config
GPIO_LED_red = 24
GPIO_LED_green = 23
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_LED_red, GPIO.OUT)
GPIO.setup(GPIO_LED_green, GPIO.OUT)

# 
ser = serial.Serial('/dev/ttyACM0', 9600, 8, 'N', 1, timeout=3)
audio_prefix = "aplay --format=S16_LE --rate=16000 " + os.getcwd()
bash_thirsty = audio_prefix + "/static_audio/thirsty.raw"
bash_satis = audio_prefix + "/static_audio/satisfied_plant.raw"
bash_watered = audio_prefix + "/static_audio/watered_plant.raw"

# Sensor Thresholds
distance_threshold = .15
soil_threshold = .40

time.sleep(4)


driver()

