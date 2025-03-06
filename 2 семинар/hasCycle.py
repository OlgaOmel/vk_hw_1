# Проверить циклический список
# Идея:
# Создаем ноду и список. В списке функция проверки.
# Делаем 2 указателя - быстрый и медленный. Быстрый через одну прыгает, а медленный идет по каждой
# Заканчиваем когда встретятся

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def hasCycle(self):
        if self.head == None or self.head.next == None:
            return False
        
        slow = self.head
        fast = self.head.next
        
        while slow != fast:
            if fast == None or fast.next == None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
        

# Тест
def test_hasCycle():
    # Тест 1: есть цикл
    my_list = LinkedList()
    node_1 = Node(11)
    my_list.head = node_1
    node_2 = Node(3)
    my_list.head.next = node_2
    node_3 = Node(8)
    node_2.next = node_3
    node_4 = Node(9)
    node_3.next = node_4
    node_5 = Node(6)
    node_4.next = node_5
    node_6 = Node(11)
    node_5.next = node_6
    node_7 = Node(16)
    node_6.next = node_7
    node_8 = Node(17)
    node_7.next = node_8
    node_8.next = node_3
    assert my_list.hasCycle() == True
    
    # Тест 2: нет цикла
    my_list = LinkedList()
    node_1 = Node(11)
    my_list.head = node_1
    node_2 = Node(3)
    my_list.head.next = node_2
    node_3 = Node(8)
    node_2.next = node_3
    node_4 = Node(9)
    node_3.next = node_4
    node_5 = Node(6)
    node_4.next = node_5
    node_6 = Node(11)
    node_5.next = node_6
    node_7 = Node(16)
    node_6.next = node_7
    node_8 = Node(17)
    node_7.next = node_8
    assert my_list.hasCycle() == False
    return True

test_hasCycle()
