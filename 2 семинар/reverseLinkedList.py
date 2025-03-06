# Развернуть односвязный список
# Создали ноду и список. Функция в списке.
# Зададим нон и голову. Проходим весь список. Следующую записываем во временню, чтобы не потерять
# И переписываем связь для нынешнего. А из временной берем новую текущую
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
    
    def reverseLinkedList(self):
        prev = None
        current = self.head
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        self.head = prev
        

# Тест
def test_reverseLinkedList():
    # Список: 1 -> 2 -> 3
    my_list = LinkedList()
    node_1 = Node(1)
    my_list.head = node_1
    node_2 = Node(2)
    my_list.head.next = node_2
    node_3 = Node(3)
    node_2.next = node_3
    # Тест 1: список создан правильно
    assert my_list.get_list() == [1, 2, 3]
    # Тест 2: список обратился назад правильно
    my_list.reverseLinkedList()
    assert my_list.get_list() == [3, 2, 1]
    return True

# Запуск теста
test_reverseLinkedList()