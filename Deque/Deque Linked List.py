class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class LinkedListDeque:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def appendleft(self, x):
        new_node = Node(x)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node
        self.size += 1

    def append(self, x):
        new_node = Node(x)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            new_node.prev = self.rear
            self.rear = new_node
        self.size += 1

    def popleft(self):
        if self.is_empty():
            raise IndexError("pop from an empty deque")
        value = self.front.data
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next
            self.front.prev = None
        self.size -= 1
        return value

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from an empty deque")
        value = self.rear.data
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.rear = self.rear.prev
            self.rear.next = None
        self.size -= 1
        return value

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def peek_front(self):
        if self.is_empty():
            raise IndexError("peek from an empty deque")
        return self.front.data

    def peek_back(self):
        if self.is_empty():
            raise IndexError("peek from an empty deque")
        return self.rear.data

def driver_code():
    deque = LinkedListDeque()

    print("Initial deque (empty):", deque.front)
    
    deque.append(10)
    deque.append(20)
    deque.append(30)
    print("\nDeque after appending 10, 20, 30:")
    print("Front:", deque.peek_front())
    print("Back:", deque.peek_back())
    print("Size:", len(deque))

    deque.appendleft(5)
    print("\nDeque after appending 5 to the front:")
    print("Front:", deque.peek_front())
    print("Back:", deque.peek_back())
    print("Size:", len(deque))

    popped_back = deque.pop()
    print("\nPopped from the back:", popped_back)
    print("Deque after popping from the back:")
    print("Front:", deque.peek_front())
    print("Back:", deque.peek_back())
    print("Size:", len(deque))

    popped_front = deque.popleft()
    print("\nPopped from the front:", popped_front)
    print("Deque after popping from the front:")
    print("Front:", deque.peek_front())
    print("Back:", deque.peek_back())
    print("Size:", len(deque))

    print("\nIs the deque empty?", deque.is_empty())

    print("\nPopping all items:")
    while not deque.is_empty():
        print("Popped item:", deque.pop())

    print("Deque after popping all items:", deque.front)
    print("Is the deque empty after popping all elements?", deque.is_empty())  # Should print True

driver_code()