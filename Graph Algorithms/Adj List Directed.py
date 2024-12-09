def add_edge(graph, node, neighbor):
    if node in graph:
        graph[node].append(neighbor)
    else:
        graph[node] = [neighbor]

graph = {
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['D'],
    'D': []
}

add_edge(graph, 'D', 'A')

print(graph)
