import socket


with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.bind(('127.0.0.1', 8888))
    while True:
        result = sock.recv(1024)
        print(result.decode())