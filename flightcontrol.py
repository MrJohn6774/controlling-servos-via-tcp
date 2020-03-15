import time
import threading
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
    a_l = threading.Thread(target=aileron_left.test)
    a_r = threading.Thread(target=aileron_right.test)
    e = threading.Thread(target=elevator.test)
    r = threading.Thread(target=rudder.test)
    a_l.start()
    a_r.start()
    e.start()
    r.start()
    a_l.join()
    a_r.join()
    e.join()
    r.join()


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

def move(js):
    while True:
        a_pos = js.getPos(0)
        e_pos = js.getPos(1)
        y_pos = js.getPos(2)
        if not a_pos:
            a_pos = 0
        if not e_pos:
            e_pos = 0
        if not y_pos:
            y_pos = 0
        gp_poses = [a_pos, e_pos, y_pos]
        aileron_left.move(gp_poses[0])
        aileron_right.move(0-gp_poses[0])
        elevator.move(gp_poses[1])
        rudder.move(gp_poses[2])
        time.sleep(0.1)


test()

try:
    ps3 = Gamepad()
    # move()
    r = threading.Thread(target=roll, args=(ps3,))
    p = threading.Thread(target=pitch, args=(ps3,))
    y = threading.Thread(target=yaw, args=(ps3,))
    w = threading.Barrier(3)
    r.start()
    p.start()
    y.start()
    r.join()
    p.join()
    y.join()

except KeyboardInterrupt:
    r.stop()
    p.stop()
    y.stop()
    Servo.cleanup()
    print("Status: Stopping...")
    Gamepad.quit()
