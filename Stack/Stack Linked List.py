class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
    
    def is_empty(self):
        return self.top is None
    
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1
    
    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        popped_data = self.top.data
        self.top = self.top.next
        self.size -= 1
        return popped_data
    
    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.top.data
    
    def get_size(self):
        return self.size

stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

print(stack.peek())

print(stack.pop())
print(stack.pop())

print(stack.is_empty())

print(stack.get_size())
