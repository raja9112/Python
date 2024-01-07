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
        
def delete_node(v):
    # Undirected, directed and unweighted graph
    # if v not in graph:
    #     print(f"{v} is not in graph")
    #     return
    # graph.pop(v)      # To remove the whole key and it's value
    # for i in graph:   # Removing "V" from Other key's list if it has
    #     list1 = graph[i]
    #     if v in list1:
    #         list1.remove(v)
            
    # {'A': ['B', 'C', 'D'], 'B': ['A', 'D'], 'C': ['A'], 'D': ['B', 'A'], 'E': []}
    # {'A': ['B', 'D'], 'B': ['A', 'D'], 'D': ['B', 'A'], 'E': []}
        
      if v not in graph:
        print(f"{v} is not in graph")
        return
      graph.pop(v)
      for i in graph:
        list1 = graph[i]
        for j in list1:
            if v == j[0]:
                list1.remove(j) 
                break
            
    # {'A': [['B', 10], ['C', 5], ['D', 8]], 'B': [['A', 10], ['D', 15]], 'C': [['A', 5]], 'D': [['B', 15], ['A', 8]], 'E': []}
    # {'A': [['B', 10], ['D', 8]], 'B': [['A', 10], ['D', 15]], 'D': [['B', 15], ['A', 8]], 'E': []}
        
def delete_edge(v1, v2, cost):
    if v1 not in graph:
        print(f"{v1} is not in graph")
    elif v2 not in graph:
        print(f"{v2} is not in graph")
    else:
        # Undirected and unweighted graph
        # For directed graphs use any one according to requirements
        # if v2 in graph[v1]:
        #     graph[v1].remove(v2) # If v2 is present in the list of v1 then the v1 is also present in the list of v2
        #     graph[v2].remove(v1)

        # For weighted graph
        list1 = [v1, cost]
        list2 = [v2, cost]
        if list2 in graph[v1]:
            graph[v1].remove(list2) 
            graph[v2].remove(list1)

        # Output
#         {'A': [['B', 10], ['C', 5], ['D', 8]], 'B': [['A', 10], ['D', 15]], 'C': [['A', 5]], 'D': [['B', 15], ['A', 8]], 'E': []}
#         {'A': [['B', 10], ['D', 8]], 'B': [['A', 10], ['D', 15]], 'C': [], 'D': [['B', 15], ['A', 8]], 'E': []}

graph = {}

add("A")
add("B")
add("C")
add("D")
add("E")
print(graph)

add_edge("A", "B", 10)
add_edge("A", "C", 5)
add_edge("B", "D", 15)
add_edge("D", "A", 8)
print(graph)

# delete_node("C")
# print(graph)

delete_edge("A", "C", 5)
print(graph)