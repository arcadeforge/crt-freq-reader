from evdev import UInput, ecodes as e

import uinput
import RPi.GPIO as GPIO
from time import sleep

events = (
    uinput.BTN_JOYSTICK,
    uinput.BTN_LEFT,
    #uinput.BTN2_JOYSTICK,
    uinput.ABS_X + (0, 255, 0, 0),
    uinput.ABS_Y + (0, 255, 0, 0),
    )

device = uinput.Device(events)

ui = UInput ()

def main():

    # center joystick
    device.emit( uinput.ABS_X, 128, syn=False )
    device.emit( uinput.ABS_Y, 128 )

    #events = (uinput.KEY_X, uinput.KEY_UP, uinput.KEY_DOWN, uinput.KEY_LEFT, uinput.KEY_RIGHT, uinput.KEY_LEFTCTRL, uinput.KEY_ENTER)
    #global device 

    #with uinput.Device(events) as device :

    global P1_UP
    #global bP1_UP

    #bP1_UP = False

    P1_UP = 4
    P1_DOWN = 17
    P1_LEFT = 27
    P1_RIGHT = 22
    P1_START = 10
    P1_SELECT = 9
    P1_TL = 14 #B3
    P1_X = 15 #B2
    P1_Y = 18 #B1
    P1_TR = 23 #B6
    P1_B = 24 #B4
    P1_A = 25 #B5

    P2_UP = 11
    P2_DOWN = 5
    P2_LEFT = 6
    P2_RIGHT = 13
    P2_START = 19
    P2_SELECT = 26
    P2_TL = 8 #B3
    P2_X = 7 #B2
    P2_Y = 12 #B1
    P2_TR = 16 #B6
    P2_B = 20 #B4
    P2_A = 21 #B5
    

    #GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(P1_UP, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    GPIO.setup(P1_DOWN, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    GPIO.setup(P1_LEFT, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    GPIO.setup(P1_RIGHT, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    GPIO.setup(P1_START, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    GPIO.setup(P1_SELECT, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    GPIO.setup(P1_TL, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    GPIO.setup(P1_X, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    GPIO.setup(P1_Y, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    GPIO.setup(P1_TR, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    GPIO.setup(P1_B, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    GPIO.setup(P1_Y, GPIO.IN, pull_up_down = GPIO.PUD_UP)

    GPIO.setup(P2_UP, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    GPIO.setup(P2_DOWN, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    GPIO.setup(P2_LEFT, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    GPIO.setup(P2_RIGHT, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    GPIO.setup(P2_START, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    GPIO.setup(P2_SELECT, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    GPIO.setup(P2_TL, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    GPIO.setup(P2_X, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    GPIO.setup(P2_Y, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    GPIO.setup(P2_TR, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    GPIO.setup(P2_B, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    GPIO.setup(P2_Y, GPIO.IN, pull_up_down = GPIO.PUD_UP)

    GPIO.add_event_detect(P1_UP, GPIO.BOTH, callback=my_callback_p1_up )
    GPIO.add_event_detect(P1_DOWN, GPIO.RISING, callback=my_callback_p1_down )
    GPIO.add_event_detect(P1_RIGHT, GPIO.RISING, callback=my_callback_p1_right )
    GPIO.add_event_detect(P1_LEFT, GPIO.RISING, callback=my_callback_p1_left )
    GPIO.add_event_detect(P1_Y, GPIO.RISING, callback=my_callback_p1_y )


    try :
        while True:

#            if (not bP1_UP) and (not GPIO.input(P1_UP)):  # Up button pressed
#                bP1_UP = True
#                device.emit(uinput.KEY_X, 1) # Press Up key
#
#            if bP1_UP and GPIO.input(P1_UP):  # Up button released
#                bP1_UP = False
#                device.emit(uinput.KEY_X, 0) # Release Up key


            pass
            #sleep (0.04)

    except KeyboardInterrupt:
        GPIO.cleanup(P1_UP)
        GPIO.cleanup(P1_DOWN)
        GPIO.cleanup(P1_LEFT)
        GPIO.cleanup(P1_RIGHT)
        GPIO.cleanup(P1_TL)
        GPIO.cleanup(P1_X)
        GPIO.cleanup(P1_Y)
        GPIO.cleanup(P1_TR)
        GPIO.cleanup(P1_B)
        GPIO.cleanup(P1_A)
        GPIO.cleanup(P1_START)
        GPIO.cleanup(P1_SELECT)
        ui.close()

    

def my_callback_p1_up (self):

    #device.emit ( uinput.BTN_JOYSTICK, 1 )
    #ui.write(e.EV_KEY, e.KEY_DOWN, 1) # KEY_A
    #ui.write(e.EV_KEY, e.KEY_DOWN, 0)
    ui.write(e.EV_KEY, e.KEY_A, 1) # KEY_A
    ui.write(e.EV_KEY, e.KEY_A, 0)
    ui.syn()


    if GPIO.input (P1_UP) :
        device.emit ( uinput.ABS_Y, 128 )
        #device.emit(uinput.KEY_UP, 0) # Press Left Ctrl key
    else:
        device.emit ( uinput.ABS_Y, 0 )
        #device.emit(uinput.KEY_UP, 1) # Press Left Ctrl key
        #print("up detected")

    sleep (0.04)

    #print("up detected")

def my_callback_p1_right (self):
    device.emit(uinput.KEY_RIGHT, 1) # Press Left Ctrl key
    sleep (0.04)
    device.emit(uinput.KEY_RIGHT, 0) # Press Left Ctrl key

    print("right detected")

def my_callback_p1_left (self):
    device.emit(uinput.KEY_LEFT, 1) # Press Left Ctrl key
    sleep (0.04)
    device.emit(uinput.KEY_LEFT, 0) # Press Left Ctrl key

    print("left detected")

def my_callback_p1_down (self):
    device.emit ( uinput.ABS_Y, 255 )
    #device.emit(uinput.KEY_DOWN, 1) # Press Left Ctrl key
    sleep (0.04)
    #device.emit(uinput.KEY_DOWN, 0) # Press Left Ctrl key
    device.emit ( uinput.ABS_Y, 128 )

    #print("down detected")

def my_callback_p1_y (self):
    device.emit(uinput.KEY_ENTER, 1) # Press Left Ctrl key
    sleep (0.04)
    device.emit(uinput.KEY_ENTER, 0) # Press Left Ctrl key


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
