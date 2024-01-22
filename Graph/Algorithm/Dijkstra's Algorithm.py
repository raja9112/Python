# NeetcodeIO
# https://neetcode.io/problems/dijkstra
# Implement Dijkstra's shortest path algorithm.

# Given a weighted, directed graph, and a starting vertex, return the shortest distance from the starting vertex to every vertex in the graph.

# Input:

# n - the number of vertices in the graph, where (2 <= n <= 100). Each vertex is labeled from 0 to n - 1.
# edges - a list of tuples, each representing a directed edge in the form (u, v, w), where u is the source vertex, v is the destination vertex, and w is the weight of the edge, where (1 <= w <= 10).
# src - the source vertex from which to start the algorithm, where (0 <= src < n).
# Note: If a vertex is unreachable from the source vertex, the shortest path distance for the unreachable vertex should be -1.

# Example 1:

# Dijkstra's Algorithm

# Input:
# n = 5
# edges = [[0,1,10], [0,2,3], [1,3,2], [2,1,4], [2,3,8], [2,4,2], [3,4,5]]
# src = 0

# Output:
# {{0:0}, {1:7}, {2:3}, {3:9}, {4:5}}


class Solution:
    # Implementation for Dijkstra's shortest path algorithm
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = {}
        for i in range(n):
            adj[i] = []
            
        # s = src, d = dst, w = weight
        for s, d, w in edges:
            adj[s].append([d, w])

        # Compute shortest paths
        shortest = {}
        minHeap = [[0, src]]
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in shortest:
                continue
            shortest[n1] = w1

            for n2, w2 in adj[n1]:
                if n2 not in shortest:
                    heapq.heappush(minHeap, [w1 + w2, n2])
        
        # Fill in missing nodes
        for i in range(n):
            if i not in shortest:
                shortest[i] = -1

        return shortest