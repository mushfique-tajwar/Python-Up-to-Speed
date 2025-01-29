class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class CircularLinkedList:
    def __init__(self):
        self.head = None
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head
    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            new_node.next = self.head
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
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
            while temp.next != self.head:
                temp = temp.next
            temp.next = self.head.next
            self.head = self.head.next
            return
        prev = None
        while temp.data != key:
            prev = temp
            temp = temp.next
            if temp == self.head:
                print("Node not found")
                return
        prev.next = temp.next
    def print_list(self):
        if not self.head:
            print("The list is empty")
            return
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(head)")
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

# Create a Circular Linked List
cll = CircularLinkedList()
# Append elements
cll.append(10)
cll.append(20)
cll.append(30)
# Prepend elements
cll.prepend(5)
# Print list
cll.print_list()
# Delete an element
cll.delete(20)
# Print updated list
cll.print_list()
# Search for an element
print(f"Is 10 present? = {cll.search(10)}")
print(f"Is 100 present? = {cll.search(100)}")