
def add_edge_matrix(matrix, src, dest):
    matrix[src][dest] = 1

n = 4

adj_matrix = [[0] * n for _ in range(n)]

add_edge_matrix(adj_matrix, 0, 1)
add_edge_matrix(adj_matrix, 1, 2)
add_edge_matrix(adj_matrix, 2, 3)

for row in adj_matrix:
    print(row)