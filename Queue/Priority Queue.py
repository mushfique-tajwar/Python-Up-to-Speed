import heapq

class PriorityQueue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item, priority):
        heapq.heappush(self.queue, (priority, item))
    
    def dequeue(self):
        if not self.queue:
            raise IndexError("Queue is empty")
        return heapq.heappop(self.queue)[1]
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def front(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.queue[0][1]

if __name__ == "__main__":
    pq = PriorityQueue()
    
    pq.enqueue("Task 1", 3)
    pq.enqueue("Task 2", 1)
    pq.enqueue("Task 3", 2)
    
    print("Front item:", pq.front())

    print("Dequeued:", pq.dequeue())
    print("Dequeued:", pq.dequeue())
    print("Dequeued:", pq.dequeue())
    
    print("Is queue empty?", pq.is_empty())
    
    try:
        pq.dequeue()
    except IndexError as e:
        print("Error:", e)