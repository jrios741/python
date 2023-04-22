class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def printlist(self):
        printhead = self.head
        while printhead is not None:
            print(printhead.data)
            printhead = printhead.next


list = LinkedList()
list.head = Node(1)
n2 = Node(2)
n3 = Node(3)

list.head.next = n2
n2.next = n3
