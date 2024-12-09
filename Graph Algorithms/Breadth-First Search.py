from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    bfs_order = []

    while queue:
        current = queue.popleft()
        if current not in visited:
            visited.add(current)
            bfs_order.append(current)

            for neighbor in graph[current]:
                if neighbor not in visited:
                    queue.append(neighbor)
    return bfs_order

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

result = bfs(graph, 'A')
print("BFS Traversal:", result)
