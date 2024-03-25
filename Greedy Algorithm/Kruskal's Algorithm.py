class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    # Find set of an element i
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    # Union of two sets of x and y
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        # Attach smaller rank tree under root of high rank tree
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal_mst(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []

        # Initialize sets of disjoint sets
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        # Number of edges to be taken is V-1
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e += 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        # Print the constructed MST
        print("Edges in the constructed MST:")
        for u, v, weight in result:
            print(f"{u} -- {v} == {weight}")


# Example usage:
g = Graph(5)
g.add_edge(0, 1, 4)
g.add_edge(0, 2, 8)
g.add_edge(1, 2, 11)
g.add_edge(1, 3, 8)
g.add_edge(2, 3, 7)
g.add_edge(2, 4, 2)
g.add_edge(3, 4, 9)

g.kruskal_mst()
