# Учитывая действительный (IPv4) IP -адрес address, вернуть защищенную версию этого IP-адреса.
# В защищенном IP-адресе  каждая точка заменяется "."на "[.]".
# Пример 1:
# Ввод: адрес = "1.1.1.1"
#  Вывод: "1[.]1[.]1[.]1"
class Solution:
    def defangIPaddr(self, address: str) -> str:
        self.address = address
        lst = list(self.address)
        for i in range(len(lst)):
            if lst[i] == '.':
                lst[i] = '[.]'
        return ''.join(lst)


a = Solution()
print(a.defangIPaddr("255.100.50.0"))