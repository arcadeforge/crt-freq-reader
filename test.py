
import RPi.GPIO as GPIO
#import sys
#import os
from time import sleep

def main():

    test_low = 17
    test_high = 27
    #GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    #GPIO.setup(test, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
    GPIO.setup(test_high, GPIO.IN, pull_up_down = GPIO.PUD_UP)

    #GPIO.setup(test_low, GPIO.IN)
    #GPIO.setup(test_high, GPIO.IN)
    #GPIO.add_event_detect(test, GPIO.BOTH, callback=my_callback_both )
    #GPIO.add_event_detect(test, GPIO.FALLING, callback=my_callback_fall )
    #GPIO.add_event_detect(test_high, GPIO.FALLING, callback=my_callback_falling )
    GPIO.add_event_detect(test_high, GPIO.RISING, callback=my_callback_rise )

    print ("test")
    try :
        while True:
            #if GPIO.input (test):
            #    print ("button released")

            pass
            #sleep (0.075)

    except KeyboardInterrupt:
        print ("cleanup")
        GPIO.cleanup(test_low)
        GPIO.cleanup(test_high)
        

def my_callback_rise (self):
    print("rise detected")

def my_callback_both (self):
    print("both detected")

def my_callback_fall (self):
    print("fall detected")


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
