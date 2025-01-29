class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class SinglyLinkedList:
    def __init__(self):
        self.head = None
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
    def insert_at_position(self, position, data):
        if position == 0:
            self.insert_at_beginning(data)
            return
        new_node = Node(data)
        temp = self.head
        for _ in range(position - 1):
            if not temp:
                raise IndexError("Position out of range")
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node
    def delete_by_value(self, value):
        if not self.head:
            return
        if self.head.data == value:
            self.head = self.head.next
            return
        temp = self.head
        while temp.next and temp.next.data != value:
            temp = temp.next
        if temp.next:
            temp.next = temp.next.next
    def search(self, value):
        temp = self.head
        while temp:
            if temp.data == value:
                return True
            temp = temp.next
        return False
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data if slow else None
    def detect_cycle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
    def length(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count
    def to_list(self):
        result = []
        temp = self.head
        while temp:
            result.append(temp.data)
            temp = temp.next
        return result

sll = SinglyLinkedList()
# Insert at the beginning
print("Inserting at the beginning:")
sll.insert_at_beginning(10)
sll.insert_at_beginning(20)
sll.insert_at_beginning(30)
sll.print_list()
# Insert at the end
print("Inserting at the end:")
sll.insert_at_end(40)
sll.insert_at_end(50)
sll.print_list()
# Insert at a specific position
print("Inserting at position 2:")
sll.insert_at_position(2, 25)
sll.print_list()
# Delete by value
print("Deleting by value (10):")
sll.delete_by_value(10)
sll.print_list()
# Search for an element
print("Searching for 25:")
print(sll.search(25))
print("Searching for 100:")
print(sll.search(100))
# Reverse the linked list
print("Reversing the linked list:")
sll.reverse()
sll.print_list()
# Find the middle element
print("Finding the middle element:")
print(sll.find_middle())
# Detect a cycle (there is no cycle here)
print("Detecting a cycle:")
print(sll.detect_cycle())
# Get the length of the list
print("Length of the list:")
print(sll.length())
# Convert the list to a Python list
print("Converting linked list to Python list:")
print(sll.to_list())