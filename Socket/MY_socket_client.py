import socket as sc


def protokol_input():
    while True:
        protokol = input('Введите протокол(1-TCP/2-UDP: ')
        if protokol == '1':
            return sc.SOCK_STREAM
        elif protokol == '2':
            return sc.SOCK_DGRAM
        else:
            print('Непрапвильный ввод')


def port_input():
    while True:
        port = int(input('Введите порт:(1024-65535): '))
        if port >= 1024 and port <= 65535:
            return port
        else:
            print('Непрапвильный ввод')


protokol = protokol_input()
port = port_input()

client = sc.socket(sc.AF_INET, protokol)

client.connect(('localhost', port))

while True:
    message = input('Введите сообщение: ')
    try:
        client.send(message.encode())
        client.close()
    except KeyboardInterrupt:
        print('Остановка')
        client.close()
