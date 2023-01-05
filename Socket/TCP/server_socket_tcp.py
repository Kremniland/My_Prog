import socket as sc

sock = sc.socket(sc.AF_INET, sc.SOCK_STREAM)
sock.bind(('localhost', 9090))

sock.listen(3)

# sock.setblocking(True)  # Вкл. блокирующий режим - Программа останавливается и ожидает подключения
# sock.setblocking(False)  # Выкл. блокирующего режима - Программа не останавливается и идет дальше

sock.settimeout(4)  # Установка времени ожидания (4 сек)
sock.settimeout(0)  # == sock.setblocking(False)
sock.settimeout(None)  # == sock.setblocking(True)

while True:
    try:
        client, addr = sock.accept()
    except KeyboardInterrupt:
        sock.close()
        break
    except sc.error:
        print("No connection")
    else:
        while True:
            result = client.recv(1024)
            if result.decode('utf-8') == 'exit':
                client.close()
                break
            print("Message: ", result.decode('utf-8'))
