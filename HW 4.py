class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = Node()
        self.head.next = self.head

    def insert_end(self, data):
        new_node = Node(data)
        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = new_node
        new_node.next = self.head

    def insert_first(self, data):
        new_node = Node(data)
        new_node.next = self.head.next
        self.head.next = new_node

    def insert_after(self, prev_data, data):
        new_node = Node(data)
        current = self.head.next
        while current != self.head and current.data != prev_data:
            current = current.next
        if current != self.head:
            new_node.next = current.next
            current.next = new_node

    def delete_first(self):
        if self.head.next != self.head:
            self.head.next = self.head.next.next

    def delete_end(self):
        if self.head.next != self.head:
            current = self.head
            while current.next.next != self.head:
                current = current.next
            current.next = self.head

    def display(self):
        if self.head.next == self.head:
            print("List is empty")
            return
        current = self.head.next
        while current != self.head:
            print(current.data, end=" -> ")
            current = current.next
        print("HEAD")
