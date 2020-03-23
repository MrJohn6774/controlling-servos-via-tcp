import socket
import threading

PORT = 1013

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", PORT))
s.listen()


def handler(conn, addr):
    with conn:
        print(f'Connection from {addr}')
        print('Servos list number', conn.recv(1).decode())
        while 1:
            data = conn.recv(18).decode()
            if not data:
                break
            print(float(data))        # move()


while 1:
    try:
        conn, addr = s.accept()
        t = threading.Thread(target=handler, args=[conn, addr], daemon=True)
        t.start()
    except KeyboardInterrupt:
        break
