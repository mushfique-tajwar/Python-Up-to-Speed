def floyd_warshall(graph):
    n = len(graph)
    
    dist = [row[:] for row in graph]
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

INF = float('inf')
graph = [
    [0, 3, INF, INF, INF, INF],
    [2, 0, INF, INF, INF, INF],
    [INF, 7, 0, 1, INF, INF],
    [6, INF, INF, 0, 2, 3],
    [INF, INF, INF, INF, 0, 1],
    [INF, INF, INF, INF, INF, 0]
]

shortest_paths = floyd_warshall(graph)

print("Shortest path distances between all pairs of vertices:")
for row in shortest_paths:
    print(row)
