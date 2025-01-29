class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            new_node.prev = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
            new_node.next = self.head
            self.head.prev = new_node
    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            new_node.prev = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    def delete(self, key):
        if not self.head:
            print("The list is empty")
            return
        temp = self.head
        if temp.data == key and temp.next == self.head:
            self.head = None
            return
        if temp.data == key:
            temp.next.prev = temp.prev
            temp.prev.next = temp.next
            self.head = temp.next
            return
        while temp.data != key:
            temp = temp.next
            if temp == self.head:
                print("Node not found")
                return
        temp.prev.next = temp.next
        temp.next.prev = temp.prev
    def print_list(self):
        if not self.head:
            print("The list is empty")
            return
        temp = self.head
        while True:
            print(temp.data, end=" <-> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(head)")
    def print_reverse(self):
        if not self.head:
            print("The list is empty")
            return
        temp = self.head.prev
        while True:
            print(temp.data, end=" <-> ")
            temp = temp.prev
            if temp == self.head.prev:
                break
        print("(tail)")
    def search(self, key):
        temp = self.head
        if not self.head:
            return False
        while True:
            if temp.data == key:
                return True
            temp = temp.next
            if temp == self.head:
                break
        return False
    
# Create a Doubly Circular Linked List
dcll = DoublyCircularLinkedList()
# Append elements
dcll.append(10)
dcll.append(20)
dcll.append(30)
# Prepend elements
dcll.prepend(5)
# Print list (forward direction)
dcll.print_list()
# Print list (reverse direction)
dcll.print_reverse()
# Delete an element
dcll.delete(20)
# Print updated list
dcll.print_list()
# Search for an element
print(dcll.search(10))
print(dcll.search(100))