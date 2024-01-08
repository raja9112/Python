def add(vertex):
    if vertex not in graph:
        graph[vertex] = []
        return
    print(f"The given node {vertex} is already present in graph")
    
# def add_edge(v1, v2):
def add_edge(v1, v2, cost):
    if v1 not in graph:
        print(f"The given node {v1} is not present in graph")
    elif v2 not in graph:
        print(f"The given node {v2} is not present in graph")
    else:
        # For undirected and unweighted graph
        # graph[v1].append(v2)
        # graph[v2].append(v1)
        
        # For undirected and weighted graph
        cost1 = [v2, cost]
        cost2 = [v1, cost]
        graph[v1].append(cost1)
        graph[v2].append(cost2)     
        
        # For directed and weighted graph
        # cost1 = [v2, cost]
        # graph[v1].append(cost1)       
        
def DFS(node, visted, graph):
    if node not in graph:
        print(f"{node} is not present in graph")
        return
    if node not in visited:
        print(node)
        visited.add(node)
        for i in graph[node]:
            # DFS(i, visted, graph)   # For unweighted graph
            DFS(i[0], visted, graph)    # For weighted graph, i[0] will check the node present in the nested loop.
            
    # Output 
    # B
    # A
    # C
    # D
    # E


visited = set()
        
graph = {}

add("A")
add("B")
add("C")
add("D")
add("E")
print(graph)

add_edge("A", "B", 10)
add_edge("B", "E", 5)
add_edge("A", "C", 15)
add_edge("A", "D", 9)
add_edge("B", "D", 6)
add_edge("C", "D", 3)
add_edge("E", "D", 1)
print(graph)

DFS("B", visited, graph)


# Complexity
# Time Complexity:
# O(V + E), where V is the number of vertices (nodes) and E is the number of edges in the graph.
# The time complexity is linear with respect to the sum of the vertices and edges because, in the worst case, DFS traverses every vertex and edge once.
# Visiting each node and its adjacent edges takes constant time per edge (assuming adjacency list representation).

# Space Complexity:
# O(V) for the visited set, where V is the number of vertices.
# The visited set is used to keep track of nodes that have been visited during the traversal. In the worst case, it can store all vertices in the graph.
# The actual time complexity can vary depending on the graph's structure, the order in which nodes are 
#     visited, and the specific implementation details. However, for a general DFS traversal on a graph represented as an adjacency list, the mentioned complexities 
#     provide an overall understanding of its performance characteristics.