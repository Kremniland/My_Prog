import socket as sc

sock = sc.socket(sc.AF_INET, sc.SOCK_DGRAM)

# sock.sendto(b'How your day?', ('localhost', 7654))
sock.connect(('127.0.0.1', 7654))
sock.send(b'Message')