class Mylist(list):
    ''' Переопределяем __getitem__ для list, что бы индекс начинался с 1'''
    def __getitem__(self, index):
        if index == 0:
            raise IndexError('Error')
        elif index < 0:
            return super().__getitem__(index)
        
        return super().__getitem__(index - 1)


lst = [1, 2, 3, 4, 5]
newlst = Mylist(lst)
print(newlst[-1])
print(Mylist.__doc__)


