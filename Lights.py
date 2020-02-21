import time
import RPi.GPIO as GPIO

def moi_check(moisture_level, led1, led2):
    if moisture_level < 60:
        GPIO.output(led1,False)
        GPIO.output(led2,True)
    else:
        GPIO.output(led2,False)
        GPIO.output(led1,True)
    return moisture_level

def butt_check(moisture_level, butt1, led1, led2):
    if GPIO.input(butt1) == 0:
        GPIO.output(led1, False)
        GPIO.output(led2, False)
        time.sleep(.3)
        GPIO.output(led1,True)
        GPIO.output(led2,True)
        moisture_level = 105
        time.sleep(.3)
        GPIO.output(led1, False)
        GPIO.output(led2, False)
        time.sleep(.3)
        GPIO.output(led1,True)
        GPIO.output(led2,False)
    else:
        pass
    return moisture_level

red_LED = 17
green_LED = 18
add_button = 2
sub_button = 26

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(red_LED, GPIO.OUT)
GPIO.setup(green_LED, GPIO.OUT)
GPIO.setup(add_button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

curr_moi = 100

while True:
    curr_moi = moi_check(curr_moi, green_LED, red_LED)
    curr_moi = butt_check(curr_moi, add_button, green_LED, red_LED)
    time.sleep(1)
    curr_moi -= 5
    GPIO.output(red_LED, False)
    time.sleep(.1)
    GPIO.output(red_LED, True)
    time.sleep(.1)
