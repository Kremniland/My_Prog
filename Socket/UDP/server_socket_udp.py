import socket as sc

# AF_INET - использование IPv4 192.168.0.101 - 256.256.256.256
# AF_INET6 - использование IPv6 2001:0bd9:7821:ae72:0000:8129:81bb:0129 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff

# SOCK_DGRAM - udp протокол SOCK_DATAGRAM

sock = sc.socket(sc.AF_INET, sc.SOCK_DGRAM)

# bind - привязывание - связывание нашего сокета с портом (8888)

sock.bind(('localhost', 8888))

# recv - receive - получить

result = sock.recv(1024) # 2^10

print("Message: ", result.decode('utf-8'))