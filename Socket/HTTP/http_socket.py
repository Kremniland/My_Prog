import socket as sc

sock = sc.socket(sc.AF_INET, sc.SOCK_STREAM)

sock.connect(('example.com', 80))

content = [
    'GET / HTTP/1.1',  # Стартовая строка
    'Host: example.com',  # Заголовок (Хост)
    'Connection: keep-alive',  # Заголовок (Тип соединения)
    'Accept: text/html',  # Заголовок (Тип возвращаемых данных)
    '\n'
]

request_http = '\n'.join(content)
print('Сформированный HTTP запрос')
print(request_http)
print('-'*20)

sock.send(request_http.encode())
result = sock.recv(65532)

print(result.decode())
