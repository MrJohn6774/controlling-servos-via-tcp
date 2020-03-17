import time
import threading
import sys
import logging
from Servo import Servo
from Gamepad import Gamepad

DEBUG = True
MODE = 1                # must be set to 1/2/3
aileron_left = 11       # GPIO pin
aileron_right = 12      # GPIO pin
elevator = 15           # GPIO pin
rudder = 16             # GPIO pin
chan_list = [aileron_left, aileron_right, elevator, rudder]

if DEBUG:
    logging.basicConfig(level=logging.DEBUG)
    Gamepad.log(logging.DEBUG)
    Servo.initialize(chan_list, debug=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)
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
        logging.debug("gp_pos value = %s" % gp_pos)
        aileron_left.move(gp_pos)
        aileron_right.move(0-gp_pos)
        time.sleep(0.1)


def pitch(js):
    while True:
        time.sleep(0.015)
        gp_pos = js.getPos(1)
        if not gp_pos:
            logging.debug("gp_pos == None")
            gp_pos = 0
        logging.debug("gp_pos value = %s" % gp_pos)
        elevator.move(gp_pos)
        time.sleep(0.085)


def yaw(js):
    while True:
        time.sleep(0.03)
        gp_pos = js.getPos(2)
        if not gp_pos:
            gp_pos = 0
        logging.debug("gp_pos value = %s" % gp_pos)
        rudder.move(gp_pos)
        time.sleep(0.07)


def main(m):
    m1, m2, a = ([] for i in range(3))
    if m == 1:
        ps3 = Gamepad(Gamepad.m1)
    elif m == 2:
        ps3 = Gamepad(Gamepad.m2)
    else:
        ps3 = Gamepad(Gamepad.m3)
    axes = [roll, pitch, yaw]
    for axis in axes:
        a.append(thread(axis, a=[ps3], daemon=True))
    for x in a:
        x.join()


if __name__ == '__main__':
    tests = test()
    for t in tests:
        t.join()

    try:
        main(MODE)
    except KeyboardInterrupt:
        Gamepad.quit()
        Servo.cleanup()
        logging.info("Stopping...")
        sys.exit()
