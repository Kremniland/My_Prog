import socket as sc

sock = sc.socket(sc.AF_INET, sc.SOCK_DGRAM)

sock.bind(('127.0.0.1', 7654))

length_message = int(input('Введите, пожалуйста, размер ожидаемого пакет: '))

while True:
    try:
        result = sock.recv(length_message)
    except KeyboardInterrupt:
        print("Программа была досрочно завершена")
        sock.close()
    except sc.error as e:
        print(e)
        print("Принять данные не удалось")
    except Exception as e:
        print(e)
        sock.close()
        break
    else:
        print("Message: ", result.decode('utf-8'))