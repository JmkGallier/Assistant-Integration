#!/usr/bin/python3

import serial
import time
import os
import RPi.GPIO as GPIO

def mainListener(ard_str):
    # Add LED functions
    # Call Distance function
    ard_tup = ard_str.readline().decode("utf-8").replace("\r\n", "").split(" ") #takes the entire message from Arduino and saves
    moist_val = float(ard_tup[0])
    dist_val = float(ard_tup[1])
    return moist_val, dist_val
    
def distDiscerner(ard_str):
    ard_tup = mainListener(ard_str)
    print(d_param)
    if d_param > dist_thres:
        waterNotification(m_param)
    else:
        pass

def ledNotification():
    pass

def waterNotification(m_param):
    if m_param <= moist_thres:
        print(m_param)
        
        os.system(bash_thirsty)
        userInteraction()
    
    elif m_param > moist_thres:
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
    
    while time_counter < 15 and m_param < moist_thres: #counts and checks moisture level for 15 times
        time_counter += 1
        ser = serial.Serial('/dev/ttyACM0', 9600, 8, 'N', 1, timeout=3)
        ard_tup = mainListener(ser)
        m_param = ard_tup[0]
        d_param = ard_tup[1]
        
        if m_param > moist_thres:
            print(m_param)
            GPIO.output(green_LED,False)
            GPIO.output(red_LED,False)
            os.system(bash_watered)
            GPIO.output(green_LED,True)
            GPIO.output(red_LED,False)
            time.sleep(5)
            GPIO.output(green_LED,False)
            GPIO.output(red_LED,False)
            
            break
        else:
            continue
        
        
def distarrPrimer(dist_val, dist_array):
    if len(dist_array) == 3:
        del dist_array[0]
        dist_array.append(dist_val)
    elif len(dist_array) < 3:
        dist_array.append(dist_val)
    elif len(dist_array) > 3:
        del dist_array[4]
        distarrPrimer(dist_val, dist_array)
    return dist_array

red_LED = 24
green_LED = 23
dist_thres = .15
moist_thres = .40
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(red_LED, GPIO.OUT)
GPIO.setup(green_LED, GPIO.OUT)

ser = serial.Serial('/dev/ttyACM0', 9600, 8, 'N', 1, timeout=3)
bash_thirsty = "aplay --format=S16_LE --rate=16000 ${HOME}/Downloads/audio_repo/thirsty.raw"
bash_satis = "aplay --format=S16_LE --rate=16000 ${HOME}/Downloads/audio_repo/satisfied_plant.raw"
bash_watered = "aplay --format=S16_LE --rate=16000 ${HOME}/Downloads/audio_repo/watered_plant.raw"

fail_counter = 0
d_level_arr = []
time.sleep(4)

while fail_counter < 50: #Change to Whilte TRUE when ready to deply device after using the Cron tool
    try:
        ser_tup = mainListener(ser)
        m_level = ser_tup[0]
        d_level = ser_tup[1]
#         d_level_arr = distarrPrimer(d_level, d_level_arr)
#         d_level = sum(d_level_arr)/len(d_level_arr)
        print(d_level)
        if m_level > moist_thres:
            GPIO.output(red_LED,False)
            GPIO.output(green_LED,True)
            continue
        elif m_level < moist_thres and d_level > dist_thres:
            GPIO.output(green_LED,False)
            GPIO.output(red_LED,True)
            waterNotification(m_level)
        elif m_level < moist_thres and d_level < dist_thres:
            GPIO.output(green_LED,False)
            GPIO.output(red_LED,False)
            pass
                
        
        fail_counter += 1
        print(fail_counter)
    except IndexError:
        continue

