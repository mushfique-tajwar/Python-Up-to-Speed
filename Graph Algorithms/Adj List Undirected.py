def add_edge_undirected(graph, node1, node2):
    if node1 not in graph:
        graph[node1] = []
    if node2 not in graph:
        graph[node2] = []
    graph[node1].append(node2)
    graph[node2].append(node1)

graph = {}

add_edge_undirected(graph, 'A', 'B')
add_edge_undirected(graph, 'A', 'C')
add_edge_undirected(graph, 'B', 'D')

print(graph)
