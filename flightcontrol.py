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


def aileron(gamepad):
    while True:
        gp_pos = gamepad.getAileron()
        if not gp_pos:
            gp_pos = 0
        print("DEBUG: gp_pos value =", gp_pos)
        aileron_left.move(gp_pos)
        aileron_right.move(0-gp_pos)
        time.sleep(0.09)

test()

try:
    ps3 = Gamepad()
    aileron(ps3)
except(KeyboardInterrupt):
    Servo.cleanup()
    Gamepad.quit()
    print("Stopped")
