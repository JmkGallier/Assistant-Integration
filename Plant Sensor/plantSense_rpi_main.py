#!/usr/bin/python3
import serial
import time
import os
import RPi.GPIO as GPIO


def mainListener(ard_str):
    ard_tup = ard_str.readline().decode("utf-8").replace("\r\n", "").split(" ")
    moist_val = float(ard_tup[0])
    dist_val = float(ard_tup[1])
    return moist_val, dist_val


def distDiscerner(ard_str):
    ard_tup = mainListener(ard_str)
    print(d_param)
    if d_param > distance_threshold:
        waterNotification(m_param)
    else:
        pass


def ledNotification():
    pass


def waterNotification(m_param):
    if m_param <= soil_threshold:
        print(m_param)
        os.system(bash_thirsty)
        userInteraction()
    
    elif m_param > soil_threshold:
        print(m_param)
        GPIO.output(green_LED,False)
        GPIO.output(red_LED,True)
        time.sleep(4)
        GPIO.output(red_LED,False)
        os.system(bash_satis)
        time.sleep(30)


def userInteraction():
    m_param = 0
    time_counter = 0
    
    while time_counter < 15 and m_param < soil_threshold: #counts and checks moisture level for 15 times
        time_counter += 1
        ser = serial.Serial('/dev/ttyACM0', 9600, 8, 'N', 1, timeout=3)
        ard_tup = mainListener(ser)
        m_param = ard_tup[0]
        d_param = ard_tup[1]
        
        if m_param > soil_threshold:
            print(m_param)
            GPIO.output(green_LED, False)
            GPIO.output(red_LED, False)
            os.system(bash_watered)
            GPIO.output(green_LED, True)
            GPIO.output(red_LED, False)
            time.sleep(5)
            GPIO.output(green_LED, False)
            GPIO.output(red_LED, False)
            
            break
        else:
            continue


red_LED = 24
green_LED = 23
distance_threshold = .15
soil_threshold = .40
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(red_LED, GPIO.OUT)
GPIO.setup(green_LED, GPIO.OUT)

ser = serial.Serial('/dev/ttyACM0', 9600, 8, 'N', 1, timeout=3)
audio_prefix = "aplay --format=S16_LE --rate=16000 " + os.getcwd()
bash_thirsty = audio_prefix + "/static_audio/thirsty.raw"
bash_satis = audio_prefix + "/static_audio/satisfied_plant.raw"
bash_watered = audio_prefix + "/static_audio/watered_plant.raw"

dev_counter = 0
time.sleep(4)

while dev_counter < 50:
    try:
        ser_tup = mainListener(ser)
        m_level = ser_tup[0]
        d_level = ser_tup[1]
        print(d_level)
        if m_level > soil_threshold:
            GPIO.output(red_LED, False)
            GPIO.output(green_LED, True)
            continue
        elif m_level < soil_threshold and d_level > distance_threshold:
            GPIO.output(green_LED, False)
            GPIO.output(red_LED, True)
            waterNotification(m_level)
        elif m_level < soil_threshold and d_level < distance_threshold:
            GPIO.output(green_LED, False)
            GPIO.output(red_LED, False)
            pass

        dev_counter += 1
        print(dev_counter)
    except IndexError:
        continue
