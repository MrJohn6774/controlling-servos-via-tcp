import argparse
import socket
import threading
import sys
import time
import logging
from Gamepad import Gamepad


parser = argparse.ArgumentParser()
parser.add_argument("host", help="Host destination IP", type=str)
parser.add_argument("-p", "--port", metavar="1013", help="Host port [Default=1013]", type=int, default=1013)
parser.add_argument("-m", "--mode", metavar="2", help="Set the mode of your controller [Default=2]", type=int, default=2)
parser.add_argument("-d", "--debug", help="Set debug mode to True", action="store_true")
args = parser.parse_args()

PORT = args.port
HOST = args.host
MODE = args.mode
DEBUG = args.debug


def thread(func, a=[], daemon=False):
    x = threading.Thread(target=func, args=a)
    if daemon:
        x.daemon = True
    x.start()
    return x


def test(s):
    pos = ["000000000000000000", "-1.000000000000000", "1.0000000000000000"]
    s.send(pos[0].encode('utf-8'))
    logging.debug("Position: Neutral")
    time.sleep(0.3)
    s.send(pos[1].encode('utf-8'))
    logging.debug("Position: Down")
    time.sleep(0.5)
    s.send(pos[2].encode('utf-8'))
    logging.debug("Position: Up")
    time.sleep(0.8)
    s.send(pos[0].encode('utf-8'))
    logging.debug("Position: Neutral")
    time.sleep(0.5)
    logging.info("Remote servo test completed.")


def move(a, js):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        if a == 1:
            s.send(str(0).encode('utf-8'))
        else:
            s.send(str(a).encode('utf-8'))
        test(s)
        while True:
            try:
                gp_pos = js.getPos(a-1)
                if not gp_pos:
                    gp_pos = "000000000000000000"
                else:
                    gp_pos = str(gp_pos)
                while(len(gp_pos) < 18):
                    gp_pos = gp_pos + "0"
                logging.debug("gp_pos value = %s" % gp_pos)
                s.sendall(gp_pos.encode('utf-8'))
                time.sleep(0.08)
            except KeyboardInterrupt:
                break


def main():
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


if __name__ == "__main__":
    try:
        if DEBUG:
            logging.basicConfig(level=logging.DEBUG)
            Gamepad.log(debug=logging.DEBUG)
        else:
            logging.basicConfig(level=logging.INFO)
            Gamepad.log()
        main()
    finally:
        logging.info("Stopping")
        Gamepad.quit()
        sys.exit()
