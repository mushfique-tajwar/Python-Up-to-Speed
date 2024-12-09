def add_edge_matrix_undirected(matrix, src, dest):
    matrix[src][dest] = 1
    matrix[dest][src] = 1

n = 4

adj_matrix = [[0] * n for _ in range(n)]

add_edge_matrix_undirected(adj_matrix, 0, 1)
add_edge_matrix_undirected(adj_matrix, 1, 2)
add_edge_matrix_undirected(adj_matrix, 2, 3)

for row in adj_matrix:
    print(row)