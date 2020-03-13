import RPi.GPIO as gpio
import time
import Servo


aileron_left = 11
aileron_right = 12
elevator = 15
rudder = 16
chan_list = [aileron_left, aileron_right, elevator, rudder]


def initialize():
    global chan_list
    gpio.setmode(gpio.BOARD)
    gpio.setup(chan_list, gpio.OUT)


def test():
    initialize()
    global aileron_left
    al = Servo(aileron_left)
    al.pwm.start(7.5)
    print("Left Aileron Down")
    time.sleep(0.2)
    al.pwm.ChangeDutyCycle(9.5)
    print("Left Aileron Up")


test()
