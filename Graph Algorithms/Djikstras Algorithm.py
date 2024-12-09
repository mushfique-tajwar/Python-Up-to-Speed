def dijkstra(graph, start):
    n = len(graph)

    distances = [float('inf')] * n
    distances[start] = 0

    visited = [False] * n

    for _ in range(n):
        min_distance = float('inf')
        min_index = -1
        for i in range(n):
            if not visited[i] and distances[i] < min_distance:
                min_distance = distances[i]
                min_index = i

        if min_index == -1:
            break

        visited[min_index] = True

        for j in range(n):
            if graph[min_index][j] > 0 and not visited[j]:
                new_distance = distances[min_index] + graph[min_index][j]
                if new_distance < distances[j]:
                    distances[j] = new_distance

    return distances

graph = [
        [0, 10, 0, 30, 100],
        [10, 0, 50, 0, 0],
        [0, 50, 0, 20, 10],
        [30, 0, 20, 0, 60],
        [100, 0, 10, 60, 0],
    ]
start_vertex = 0

print("Shortest distances from vertex", start_vertex, "are:")
print(dijkstra(graph, start_vertex))
