import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(('example.com', 80))

connect = [
    'GET / HTTP/1.1',  # Стартовая строка
    'Host: example.com',  # Заголовок (Хост)
    'Connection: keep-alive',  # Заголовок (Тип соединения)
    'Accept: text/html',  # Заголовок (Тип возвращаемых данных)
    '\n'
]

request_http = '\n'.join(connect)

print(request_http)

sock.send(request_http.encode())
result = sock.recv(65532)

print(result.decode())