#blink to pwm

import RPi.GPIO as GPIO
import time



#cycle between the two


x = 0
while True:
    print("running sequence...")
    GPIO.setmode(GPIO.BCM)
    led_pin = 18 #pin number
    GPIO.setup(led_pin,GPIO.OUT)
    pwm_led = GPIO.PWM(led_pin, 500)

               
    #blink
    while x < 3:
        try:
            while True and x < 3:                   
                print("blinking...")
                x += 1
                GPIO.output(led_pin, True)
                time.sleep(0.25)
                GPIO.output(led_pin, False)
                time.sleep(0.25)
        finally:
            print("cleaning blink...")
            GPIO.cleanup()

    #pwm   
    while x > 0:
        try:           
            while True and x > 0:           
                print("pulsing...")
                x -= 1                   
                pwm_led.start(0)

                y = 0
                while y < 100:
                    y += 1
                    pwm_led.ChangeDutyCycle(y)
                while y > 0:
                    y -= 1
                    pwm_led.ChangeDutyCycle(y)
        finally:
            print("cleaning pulse...")
            GPIO.cleanup()       

