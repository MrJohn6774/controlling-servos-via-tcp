import time
import threading
import sys
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
servos = [aileron_left, aileron_right, elevator, rudder]


def thread(func, a=[], daemon=False):
    x = threading.Thread(target=func, args=a)
    if daemon:
        x.daemon = True
    x.start()
    return x


def test():
    ts = []
    for servo in servos:
        ts.append(thread(servo.test))
    return ts


def roll(js):
    while True:
        gp_pos = js.getPos(0)
        if not gp_pos:
            gp_pos = 0
        print("DEBUG: gp_pos value =", gp_pos)
        aileron_left.move(gp_pos)
        aileron_right.move(0-gp_pos)
        time.sleep(0.1)


def pitch(js):
    while True:
        gp_pos = js.getPos(1)
        if not gp_pos:
            print("DEBUG: gp_pos NOT SET")
            gp_pos = 0
        print("DEBUG: gp_pos value =", gp_pos)
        elevator.move(gp_pos)
        time.sleep(0.09)


def yaw(js):
    while True:
        time.sleep(0.02)
        gp_pos = js.getPos(2)
        if not gp_pos:
            gp_pos = 0
        print("DEBUG: gp_pos value =", gp_pos)
        rudder.move(gp_pos)
        time.sleep(0.07)


tests = test()
for t in tests:
    t.join()

try:
    ps3 = Gamepad()
    axes = [roll, pitch, yaw]
    a = []
    for axis in axes:
        a.append(thread(axis, a=[ps3], daemon=True))
    for x in a:
        x.join()

except KeyboardInterrupt:
    Servo.cleanup()
    Gamepad.quit()
    print("Status: Stopping...")
    sys.exit()
