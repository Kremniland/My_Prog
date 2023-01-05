import socket as sc

sock = sc.socket(sc.AF_INET, sc.SOCK_STREAM)

sock.connect(('127.0.0.1', 9090)) # Соединение с получателем
# После успешного соединения
sock.send(b'Hello TCP from second client') # Отправка сообщения

sock.close() # Закрытие сокета - разрыв соединения