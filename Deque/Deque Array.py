class ArrayDeque:
    def __init__(self):
        self.deque = []

    def append(self, x):
        self.deque.append(x)

    def appendleft(self, x):
        self.deque.insert(0, x)

    def pop(self):
        if not self.deque:
            raise IndexError("pop from an empty deque")
        return self.deque.pop()

    def popleft(self):
        if not self.deque:
            raise IndexError("pop from an empty deque")
        return self.deque.pop(0)

    def __len__(self):
        return len(self.deque)

    def is_empty(self):
        return len(self.deque) == 0

def driver_code():
    deque = ArrayDeque()
    
    print("Initial deque:", deque.deque)
    
    deque.append(10)
    deque.append(20)
    deque.append(30)
    print("Deque after appending 10, 20, 30:", deque.deque)
    
    deque.appendleft(5)
    print("Deque after appending 5 to the left:", deque.deque)
    
    popped_item = deque.pop()
    print("Popped item from the right:", popped_item)
    print("Deque after popping from the right:", deque.deque)
    
    popped_item_left = deque.popleft()
    print("Popped item from the left:", popped_item_left)
    print("Deque after popping from the left:", deque.deque)
    
    print("Length of deque:", len(deque))
    
    print("Is the deque empty?", deque.is_empty())
    
    while not deque.is_empty():
        print("Popped item:", deque.pop())
    print("Deque after popping all items:", deque.deque)
    print("Is the deque empty after popping all elements?", deque.is_empty())

# Run the driver code
driver_code()
