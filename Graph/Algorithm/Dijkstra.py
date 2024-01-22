import sys

class Algo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0] * vertices for _ in range(vertices)]
        
    def min_distance(self, dist, spt_set):
        min_dist = sys.maxsize
        min_index = -1
        
        for v in range(self.vertices):
            if dist[v] < min_dist and not spt_set[v]:
                min_dist = dist[v]
                min_index = v 
            
        return min_index
    
    def Dijkstra(self, src):
        dist = [sys.maxsize] * self.vertices
        dist[src] = 0
        spt_set = [False] * self.vertices
        
        for _ in range(self.vertices):
            u = self.min_distance(dist, spt_set)
            spt_set[u] = True
            
            for v in range(self.vertices):
                if not spt_set[v] and self.graph[u][v] != 0 and dist[u] + self.graph[u][v] < dist[v]:
                    dist[v] = dist[u] + self.graph[u][v]
                    
        self.print_solution(dist)
         
    def print_solution(self, dist):
        print("Vertex \tDistance from Source")
        for node in range(self.vertices):
            print(node, "\t", dist[node])

graph = Algo(9)
graph.graph = [
    [0, 4, 0, 0, 0, 0, 0, 8, 0],
    [4, 0, 8, 0, 0, 0, 0, 11, 0],
    [0, 8, 0, 7, 0, 4, 0, 0, 2],
    [0, 0, 7, 0, 9, 14, 0, 0, 0],
    [0, 0, 0, 9, 0, 10, 0, 0, 0],
    [0, 0, 4, 14, 10, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 1, 6],
    [8, 11, 0, 0, 0, 0, 1, 0, 7],
    [0, 0, 2, 0, 0, 0, 6, 7, 0],
]

graph.Dijkstra(0)

# Output
# Vertex  Distance from Source
# 0        0
# 1        4
# 2        12
# 3        19
# 4        21
# 5        11
# 6        9
# 7        8
# 8        14

# Imports the sys module, which is used to get the maximum size of integers (sys.maxsize).
# Defines a class named Dijkstra.
# __init__: Constructor method that initializes the object. It takes the number of vertices in the graph as a parameter and initializes the graph attribute as an adjacency matrix filled with zeros.
# min_distance: Helper method to find the vertex with the minimum distance value that has not been included in the shortest path set (spt_set).
# It iterates through all vertices, checks if the distance is smaller than the current minimum distance, and if the vertex is not in the shortest path set.
# dijkstra: Main method to perform Dijkstra's algorithm. It takes the source vertex (src) as a parameter.
# Initializes the distance array (dist) with infinity for all vertices, sets the distance of the source vertex to 0, and initializes the shortest path set (spt_set) to False for all vertices.
# Iterates through all vertices and selects the vertex u with the minimum distance from the source that has not been processed.
# Updates the shortest path set for u and relaxes the distances of its neighbors.
# Calls the print_solution method to print the final results.