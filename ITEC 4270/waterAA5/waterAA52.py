import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
switch_pin = 23

GPIO.setup(switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

goal = 8
counter = 0
goalreached = False

while True:
    if GPIO.input(switch_pin) == False:
        if goal != counter: 
            counter +=1
            print(counter)
            time.sleep(0.3)
                
        elif goal == counter and goalreached == False:  
            print("number " + str(goal) + " reached!")
            goalreached = True

    
