'''Односвязанные списки и работа с ними'''

class Node:
    '''создание односвязанного списка'''
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f'{self.data}->{self.next}'

class LinkedList:
    def __int__(self):
        self.head = None

    def __str__(self):
        return str(self.head)

    def length(self):
        '''Длинна связанного списка'''
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count


if __name__ == '__main__':
    # Создаем элементы
    node1 = Node(1)
    node2 = Node(2)
    # Связываем их
    node1.next = node2
    print(node1)

    # Создаем в цикле связанный список
    linked_list = LinkedList()
    temp = Node(1)
    linked_list.head = temp
    for i in range(2, 5):
        temp.next = Node(i)
        temp = temp.next

    print(linked_list)
    print(linked_list.length())