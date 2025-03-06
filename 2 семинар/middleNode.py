# Найти середину списка
# Идея:
# Медленный и быстрый указатели в начало. Быстрый бежит через 1.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def show_nodes(self):
        nodes = []
        tmp = self.head
        while tmp:
            nodes.append(tmp.data)
            tmp = tmp.next
        return nodes
    
    def middleNode(self):
        slow = fast = self.head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow



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

node_6 = Node(11)
node_5.next = node_6

node_7 = Node(16)
node_6.next = node_7
def test_middleNode():
    assert my_list.middleNode().data == 9
    return True

test_middleNode()
