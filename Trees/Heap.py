import heapq

# 1. Creating a Min-Heap
data = [5, 7, 9, 1, 3]
heapq.heapify(data)  # Converts list into a heap
print("Heapified Data:", data)  # Output: [1, 3, 9, 7, 5]

# 2. Inserting into the Heap
heapq.heappush(data, 2)
print("After Push:", data)  # Output: [1, 2, 9, 7, 5, 3]

# 3. Removing the Smallest Element
smallest = heapq.heappop(data)
print("Popped Smallest:", smallest)  # Output: 1
print("After Pop:", data)           # Output: [2, 3, 9, 7, 5]

# 4. Push and Pop in One Operation
result = heapq.heappushpop(data, 4)
print("Pushpop Result:", result)  # Output: 2
print("After Pushpop:", data)     # Output: [3, 4, 9, 7, 5]

# 5. Replace the Smallest Element
result = heapq.heapreplace(data, 6)
print("Heapreplace Result:", result)  # Output: 3
print("After Heapreplace:", data)     # Output: [4, 5, 9, 7, 6]

# 6. Finding N Smallest or Largest Elements
data = [1, 3, 5, 7, 9]
smallest_two = heapq.nsmallest(2, data)
largest_two = heapq.nlargest(2, data)
print("2 Smallest:", smallest_two)  # Output: [1, 3]
print("2 Largest:", largest_two)    # Output: [9, 7]

# 7. Using Custom Key Functions
people = [{'name': 'A', 'age': 30}, {'name': 'B', 'age': 20}, {'name': 'C', 'age': 25}]
youngest_two = heapq.nsmallest(2, people, key=lambda x: x['age'])
print("2 Youngest:", youngest_two)  # Output: [{'name': 'B', 'age': 20}, {'name': 'C', 'age': 25}]

# 8. Simulating a Max-Heap
max_heap = []
heapq.heappush(max_heap, -1 * 10)  # Push -10 to simulate Max-Heap
heapq.heappush(max_heap, -1 * 20)
heapq.heappush(max_heap, -1 * 5)
max_val = -1 * heapq.heappop(max_heap)
print("Max Heap Popped Value:", max_val)  # Output: 20
