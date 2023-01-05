import socket as sc


def port_input():
    while True:
        port = int(input('Введите порт:(1024-65535): '))
        if port >= 1024 and port <= 65535:
            return port
        else:
            print('Непрапвильный ввод')


def protokol_input():
    while True:
        protokol = input('Введите протокол(1-TCP/2-UDP: ')
        if protokol == '1':
            return sc.SOCK_STREAM
        elif protokol == '2':
            return sc.SOCK_DGRAM
        else:
            print('Непрапвильный ввод')


protokol = protokol_input()
serv = sc.socket(sc.AF_INET, protokol)

port = port_input()

len_message = int(input('Ведите длинну сообщения: '))

serv.bind(('localhost', port))

if protokol == sc.SOCK_STREAM:
    list_len = int(input('Введите длинну списка: '))
    serv.listen(list_len)
    while True:
        try:
            client_socket, address = serv.accept()
        except KeyboardInterrupt:
            print('Что-то пошло не так!')
            serv.close()
            break
        else:
            result = client_socket.recv(len_message)
            client_socket.close()
            print(result.decode())
else:
    while True:
        try:
            result = serv.recv(len_message)
        except KeyboardInterrupt:
            print('Что-то пошло не так!')
            serv.close()
            break
        else:
            print(result.decode())

