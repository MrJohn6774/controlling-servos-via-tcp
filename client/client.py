import socket
import threading
import sys
import time
import logging
from Gamepad import Gamepad


PORT = 1013
HOST = "192.168.137.201"
MODE = 3
DEBUG = True


def thread(func, a=[], daemon=False):
    x = threading.Thread(target=func, args=a)
    if daemon:
        x.daemon = True
    x.start()
    return x


def move(a, js):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        if a == 1:
            s.send(str(0).encode('utf-8'))
        else:
            s.send(str(a).encode('utf-8'))
        while True:
            gp_pos = js.getPos(a-1)
            if not gp_pos:
                gp_pos = 0
            gp_pos = str(gp_pos)
            while(len(gp_pos) < 18):
                gp_pos = gp_pos + "0"
            logging.debug("gp_pos value = %s" % gp_pos)
            s.sendall(gp_pos.encode('utf-8'))
            time.sleep(0.08)


def main():
    m1, m2, a = ([] for i in range(3))
    if MODE == 1:
        ps3 = Gamepad(Gamepad.m1)
    elif MODE == 2:
        ps3 = Gamepad(Gamepad.m2)
    else:
        ps3 = Gamepad(Gamepad.m3)
    axes = [1, 2, 3]
    for axis in axes:
        a.append(thread(move, a=[axis, ps3], daemon=True))
    for x in a:
        x.join()


if __name__ == "__main__":
    try:
        if DEBUG:
            logging.basicConfig(level=logging.DEBUG)
        else:
            logging.basicConfig(level=logging.INFO)
        main()
    finally:
        logging.info("Stopping")
        sys.exit()
