from urllib import request

responce = request.urlopen('http://example.com')

print(responce)

print('Атрибут status:', responce.status)
print('Метод getcode():', responce.getcode())
print('Атрибут msg:', responce.msg)
print('Атрибут reason:', responce.reason)
print()

print('Заголовок:', responce.headers)
print()
print('Заголовок:', responce.getheaders())
print()
print('Заголовок Cache-Control:', responce.headers.get('Cache-Control'))
print()
print('Заголовок Date:', responce.getheader('Date'))
print()
print('URL', responce.url)
