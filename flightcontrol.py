import time
from Servo import Servo
from Gamepad import Gamepad


aileron_left = 11
aileron_right = 12
elevator = 15
rudder = 16
chan_list = [aileron_left, aileron_right, elevator, rudder]


Servo.initialize(chan_list)
aileron_left = Servo(chan_list[0], "Left Aileron")
aileron_right = Servo(chan_list[1], "Right Aileron")
elevator = Servo(chan_list[2], "Elevator")
rudder = Servo(chan_list[3], "Yaw")


def test():
    aileron_left.test()
    aileron_right.test()
    elevator.test()
    rudder.test()


def aileron():
    ps3 = Gamepad()
    while True:
        ps3.getAileron()


test()

try:
    aileron()
except(KeyboardInterrupt):
    Servo.cleanup()
    Gamepad.quit()
