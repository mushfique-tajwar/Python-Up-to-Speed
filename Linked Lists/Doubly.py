class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        new_node.prev = last_node
    def insert_after(self, prev_node_data, data):
        new_node = Node(data)
        temp = self.head
        while temp:
            if temp.data == prev_node_data:
                new_node.next = temp.next
                new_node.prev = temp
                if temp.next:
                    temp.next.prev = new_node
                temp.next = new_node
                return
            temp = temp.next
    def delete(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            if self.head:
                self.head.prev = None
            temp = None
            return
        while temp:
            if temp.data == key:
                if temp.next:
                    temp.next.prev = temp.prev
                if temp.prev:
                    temp.prev.next = temp.next
                temp = None
                return
            temp = temp.next
    def delete_first(self):
        if not self.head:
            return
        temp = self.head
        if temp.next:
            temp.next.prev = None
        self.head = temp.next
        temp = None
    def delete_last(self):
        if not self.head:
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        if temp.prev:
            temp.prev.next = None
        temp = None
    def traverse_forward(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
    def traverse_backward(self):
        temp = self.head
        while temp and temp.next:
            temp = temp.next
        while temp:
            print(temp.data, end=" ")
            temp = temp.prev
    def is_empty(self):
        return self.head is None
    def find(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False
    def print_list_forward(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()
    def print_list_backward(self):
        temp = self.head
        while temp and temp.next:
            temp = temp.next
        while temp:
            print(temp.data, end=" ")
            temp = temp.prev
        print()
dll = DoublyLinkedList()

dll.insert_at_beginning(10)
dll.insert_at_beginning(20)
dll.insert_at_beginning(30)

dll.print_list_forward()
dll.print_list_backward()

dll.insert_at_end(40)
dll.insert_at_end(50)

dll.print_list_forward()
dll.print_list_backward()

dll.insert_at_end(60)
dll.insert_at_beginning(5)

dll.print_list_forward()
dll.print_list_backward()