class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []

    def add_edge(self, u, v, weight):
        self.edges.append((weight, u, v))

    def find(self, parent, vertex):
        if parent[vertex] == vertex:
            return vertex
        return self.find(parent, parent[vertex])

    def union(self, parent, rank, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)

        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

    def kruskal(self):
        self.edges.sort()

        parent = [i for i in range(self.vertices)]
        rank = [0] * self.vertices

        mst = []
        mst_cost = 0

        for weight, u, v in self.edges:
            root_u = self.find(parent, u)
            root_v = self.find(parent, v)

            if root_u != root_v:
                mst.append((u, v, weight))
                mst_cost += weight
                self.union(parent, rank, root_u, root_v)

        return mst, mst_cost

g = Graph(5)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)

mst, mst_cost = g.kruskal()
print("Edges in the Minimum Spanning Tree:")
for u, v, weight in mst:
    print(f"Edge {u} - {v} with weight {weight}")
print(f"Total cost of the MST: {mst_cost}")