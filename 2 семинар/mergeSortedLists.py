# Слияние двух отсортированных списков
# Идея:
# Создали ноду и список с функцией внутри. 
# Создаем игрушечную ноду для указателя на текущую ноду и ставим указатели на начало списков
# Сравниваем значения нод пока не закончатся списки
# Меньшее значение добавляем в новый список и текущий указатель перемещается на эту ноду
# Оставшиеся ноды в конце списка
# За игрушечной нодой добавили объединение

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def get_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result
            
    
def mergeSortedLists(l1, l2):
    dummy = Node(0)
    current = dummy

    left1 = l1.head
    left2 = l2.head
    
    while left1 != None and left2 != None:
        if left1.data < left2.data:
            current.next = left1
            left1 = left1.next
        else:
            current.next = left2
            left2 = left2.next
        current = current.next
    
    if left1 != None:
        current.next = left1
    else:
        current.next = left2
    
    merged_list = LinkedList()
    merged_list.head = dummy.next
    return merged_list


# Тест
def test_mergeSortedLists():
    
    my_list1 = LinkedList()
    node_1 = Node(3)
    my_list1.head = node_1
    node_2 = Node(6)
    my_list1.head.next = node_2
    node_3 = Node(8)
    node_2.next = node_3


    my_list2 = LinkedList()
    node_4 = Node(4)
    my_list2.head = node_4
    node_5 = Node(7)
    my_list2.head.next = node_5
    node_6 = Node(9)
    node_5.next = node_6
    node_7 = Node(11)
    node_6.next = node_7
    
    print('List 1: ' + str(my_list1.get_list()))
    print('List 2: ' + str(my_list2.get_list()))
    assert mergeSortedLists(my_list1, my_list2).get_list() == [3, 4, 6, 7, 8, 9, 11]
    return True

test_mergeSortedLists()
