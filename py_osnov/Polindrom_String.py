# Переворачиваем строку и сравниваем:
def reversed4(variable):
    res=''.join(reversed(variable))
    if res == variable:
        return True
    else:
        return False


n = reversed4(input())
print(n)