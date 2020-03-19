import RPi.GPIO as gpio
import time


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
    pwm = gpio.PWM(aileron_left, 50)
    pwm.start(7)
    print("Left Aileron Neutral")
    time.sleep(0.5)
    pwm.ChangeDutyCycle(2.7)
    print("Left Aileron Down")
    time.sleep(1.5)
    pwm.ChangeDutyCycle(11.3)
    print("Left Aileron Up")
    time.sleep(1.5)
    pwm.ChangeDutyCycle(7)
    print("Left Aileron Neutral")
    time.sleep(2)
    gpio.cleanup()
    print("cleanup")


test()
