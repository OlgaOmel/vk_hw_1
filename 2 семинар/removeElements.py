# Удалить элемент из односвязного списка
# Идея:
# Сделали игрушечную ноду. Идем по списку пока не нашли нужное число.
# Переписываем у предыдущего связь на следующее за cur.
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
    def removeElements(self, data):
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy
        cur = self.head
        while cur != None:
            if cur.data == data:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next
        
        
        self.head = dummy.next
        return dummy.next
# Тест
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
node_6 = Node(12)
node_5.next = node_6
node_7 = Node(16)
node_6.next = node_7

def test_removeElements():
    my_list.removeElements(9)
    assert my_list.get_list() == [11, 3, 8, 6, 12, 16]
    # 1 элемент
    my_list.removeElements(11)
    assert my_list.get_list() == [3, 8, 6, 12, 16]
    return True

test_removeElements()    