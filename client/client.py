import socket
import threading
import sys
import time
import logging
from Gamepad import Gamepad


PORT = 1013
HOST = "192.168.137.201"
MODE = 3


def thread(func, a=[], daemon=False):
    x = threading.Thread(target=func, args=a)
    if daemon:
        x.daemon = True
    x.start()
    return x


def roll(js):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b"0")
        while True:
            gp_pos = js.getPos(0)
            if not gp_pos:
                gp_pos = 0
            logging.debug("gp_pos value = %s" % gp_pos)
            time.sleep(0.1)
            s.sendall(str(gp_pos).encode('utf-8'))


def pitch(js):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.send(b"2")
        while True:
            time.sleep(0.015)
            gp_pos = js.getPos(1)
            if not gp_pos:
                logging.debug("gp_pos == None")
                gp_pos = 0
            logging.debug("gp_pos value = %s" % gp_pos)
            time.sleep(0.085)
            s.sendall(str(gp_pos).encode('utf-8'))


def yaw(js):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.send(b"3")
        while True:
            try:
                time.sleep(0.03)
                gp_pos = js.getPos(2)
                if not gp_pos:
                    gp_pos = 0
                logging.debug("gp_pos value = %s" % gp_pos)
                time.sleep(0.07)
                s.sendall(str(gp_pos).encode('utf-8'))
            except KeyboardInterrupt:
                break


def main():
    m1, m2, a = ([] for i in range(3))
    if MODE == 1:
        ps3 = Gamepad(Gamepad.m1)
    elif MODE == 2:
        ps3 = Gamepad(Gamepad.m2)
    else:
        ps3 = Gamepad(Gamepad.m3)
    axes = [roll, pitch, yaw]
    for axis in axes:
        a.append(thread(axis, a=[ps3], daemon=True))
    for x in a:
        x.join()


if __name__ == "__main__":
    try:
        main()
    finally:
        logging.info("Stopping")
        sys.exit()
