import heapq

def dijkstra(graph, source):
    dist = {vertex: float('inf') for vertex in graph}
    dist[source] = 0
    
    pq = [(0, source)]  # (Distance, vertex)
    
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        
        if current_distance > dist[current_vertex]:
            continue
        
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance+ weight
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
            
    return dist

# Example usage:
graph = {
    'A': {'B': 2, 'C': 5, 'D': 1},
    'B': {'A': 2, 'E': 3},
    'C': {'A': 5, 'D': 1, 'E': 1},
    'D': {'A': 1, 'C': 1, 'E': 6},
    'E': {'B': 3, 'C': 1, 'D': 6}
}
source_vertex = 'A'

shortest_distances = dijkstra(graph, source_vertex)
print("Shortest distances from", source_vertex, "to each vertex:", shortest_distances)

# Dijkstra's algorithm is a perfect example of a greedy algorithm for finding single-source shortest paths in a weighted graph. Let's break down how Dijkstra's algorithm works in a greedy manner:

# Initialization:

# Initialize an array dist to store the shortest distance from the source vertex to each vertex in the graph.
# Initialize a priority queue (or a min-heap) to store vertices based on their tentative distances from the source vertex.
# Set the distance of the source vertex to 0 and all other vertices to infinity.
# Add all vertices to the priority queue with their tentative distances.
# Main Loop:

# Repeat until the priority queue is empty:
# Extract the vertex with the minimum tentative distance from the priority queue.
# For each neighbor of the extracted vertex:
# Relax the neighbor: Update its tentative distance if the sum of the current vertex's distance and the weight of the edge to the neighbor is less than the neighbor's current tentative distance.
# If the tentative distance of the neighbor is updated, update its position in the priority queue accordingly.
# Termination:

# When the priority queue is empty, all vertices have been processed, and the shortest distance from the source vertex to each vertex in the graph is determined.