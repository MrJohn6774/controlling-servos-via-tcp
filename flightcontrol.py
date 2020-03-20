import time
import threading
import socket
import sys
import logging
from Servo import Servo
from Gamepad import Gamepad

DEBUG = True
PORT = 1013
MODE = 3                # must be set to 1/2/3
aileron_left = 11       # GPIO pin
aileron_right = 12      # GPIO pin
elevator = 15           # GPIO pin
rudder = 16             # GPIO pin
channels = [aileron_left, aileron_right, elevator, rudder]

if DEBUG:
    logging.basicConfig(level=logging.DEBUG)
    Gamepad.log(logging.DEBUG)
    Servo.initialize(channels, debug=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)
    Servo.initialize(channels)

ser_names, servos = (["Left Aileron", "Right Aileron", "Elevator", "Yaw"], [])
for channel, ser_name in zip(channels, ser_names):
    servos.append(Servo(channel, ser_name))         # servos = [aileron_left, aileron_right, elevator, rudder]


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


def move(a, js):
    while True:
        gp_pos = js.getPos(a-1)
        if not gp_pos:
            gp_pos = 0
        logging.debug("gp_pos value = %s" % gp_pos)
        if a == 1:
            servos[a].move(0-gp_pos)
            servos[0].move(gp_pos)
        else:
            servos[a].move(gp_pos)
        time.sleep(0.1)


def handler(conn, addr):
    with conn:
        logging.info(f'Connection from {addr}')
        axis = int(conn.recv(1).decode())
        while 1:
            data = conn.recv(1024).decode()
            if not data:
                break
            servos[axis].move(float(data))        # move()
            if axis == 0:
                servos[axis+1].move(0-float(data))


def main():
    if Gamepad.device_count() == 0:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(("", PORT))
        s.listen()
        while 1:
            try:
                conn, addr = s.accept()
                t = threading.Thread(target=handler, args=[conn, addr], daemon=True)
                t.start()
            except KeyboardInterrupt:
                raise KeyboardInterrupt
    else:
        if MODE == 1:
            ps3 = Gamepad(Gamepad.m1)
        elif MODE == 2:
            ps3 = Gamepad(Gamepad.m2)
        else:
            ps3 = Gamepad(Gamepad.m3)
        axes, a = ([1, 2, 3], [])
        for axis in axes:
            a.append(thread(move, a=[axis, ps3], daemon=True))
        for x in a:
            x.join()


if __name__ == '__main__':
    tests = test()
    for t in tests:
        t.join()

    try:
        main()
    except KeyboardInterrupt:
        Gamepad.quit()
        Servo.cleanup()
        logging.info("Stopping...")
        sys.exit()
