import socket as sc

sock = sc.socket(sc.AF_INET, sc.SOCK_STREAM)

sock.connect(('127.0.0.1', 9090)) # Соединение с получателем
# После успешного соединения

while True:
    message = input('Напишите сообщение: ')
    sock.send(message.encode('utf-8')) # Отправка сообщения
    if message == 'exit':
        sock.close()  # Закрытие сокета - разрыв соединения
        break



