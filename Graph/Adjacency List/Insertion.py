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
        graph[v2].append(cost2)     # {'A': [['B', 10], ['C', 5]], 'B': [['A', 10]], 'C': [['A', 5]]}
        
        # For directed and weighted graph
        # cost1 = [v2, cost]
        # graph[v1].append(cost1)       # {'A': [['B', 10], ['C', 5]], 'B': [], 'C': []}
        
        
graph = {}

add("A")
add("B")
add("C")
print(graph)

add_edge("A", "B", 10)
add_edge("A", "C", 5)
print(graph)