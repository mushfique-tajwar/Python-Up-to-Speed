class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
    
    def is_empty(self):
        return self.size == 0
    
    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        
        self.size += 1
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        
        dequeued_data = self.front.data
        self.front = self.front.next
        
        if self.front is None:
            self.rear = None
        
        self.size -= 1
        return dequeued_data
    
    def front_element(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.front.data
    
    def queue_size(self):
        return self.size

if __name__ == "__main__":
    q = Queue()
    
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    
    print("Front element:", q.front_element())
    
    print("Dequeued:", q.dequeue())
    print("Dequeued:", q.dequeue())
    
    print("Queue size:", q.queue_size())
    
    print("Dequeued:", q.dequeue())
    
    print("Is the queue empty?", q.is_empty())
    
    try:
        q.dequeue()
    except IndexError as e:
        print("Error:", e)
