import socket
import time

PORT = 1013

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("127.0.0.1", PORT))
    s.sendall(b"TEST")
    while 1:
        msg = -101    # getPos()
        s.sendall(str(msg).encode('utf-8'))
        time.sleep(1)
