def prims_algorithm(graph):
    n = len(graph)

    in_mst = [False] * n

    min_edge = [float('inf')] * n

    parent = [-1] * n

    min_edge[0] = 0

    for _ in range(n):
        min_weight = float('inf')
        u = -1
        for i in range(n):
            if not in_mst[i] and min_edge[i] < min_weight:
                min_weight = min_edge[i]
                u = i

        in_mst[u] = True

        for v in range(n):
            if graph[u][v] > 0 and not in_mst[v] and graph[u][v] < min_edge[v]:
                min_edge[v] = graph[u][v]
                parent[v] = u

    mst = []
    for i in range(1, n):
        mst.append((parent[i], i, graph[i][parent[i]]))

    return mst

graph = [
        [0, 2, 0, 6, 0],
        [2, 0, 3, 8, 5],
        [0, 3, 0, 0, 7],
        [6, 8, 0, 0, 9],
        [0, 5, 7, 9, 0],
    ]

mst = prims_algorithm(graph)
print("Edges in the Minimum Spanning Tree:")
for u, v, weight in mst:
        print(f"Edge {u} - {v} with weight {weight}")
