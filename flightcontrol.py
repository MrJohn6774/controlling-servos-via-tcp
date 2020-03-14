import RPi.GPIO as gpio
import Servo


aileron_left = 11
aileron_right = 12
elevator = 15
rudder = 16
chan_list = [aileron_left, aileron_right, elevator, rudder]


def initialize():
    gpio.setmode(gpio.BOARD)
    gpio.setup(chan_list, gpio.OUT)


def test():
    initialize()
    aileron_left = Servo(chan_list[0])
    aileron_right = Servo(chan_list[1])
    elevator = Servo(chan_list[2])
    rudder = Servo(chan_list[3])
    aileron_left.test(chan_list[0])
    aileron_right.test(chan_list[1])
    elevator.test(chan_list[2])
    rudder.test(chan_list[3])


test()
