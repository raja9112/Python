def add(vertex):
    global node_count      # Need to call the node_count as global variable to modify
    if vertex in nodes:
        print(f"{vertex} is already available in graph...")
        return
    node_count += 1
    nodes.append(vertex)
    for col in graph:
        col.append(0)       # Lopping through row present in graph to add column value 0 at the end every row 
    temp_row = []
    for row in range(node_count):
        temp_row.append(0)  # Created the list to row values and appending values based on how much nodes present in nodes list
    graph.append(temp_row)  # Adding the new row in graph
    
# For undirected and directed graph
def add_edge(v1, v2): 
# def add_edge(v1, v2, cost):      # Add extra parameter if it is a weighted graph and give weight as an argument
    if v1 not in nodes:
        print(f"The {v1} is available in graph...")
    elif v2 not in nodes:
        print(f"The {v2} is available in graph...")
    else:
        index1 = nodes.index(v1)        # Getting a index of the given vertices from nodes list
        index2 = nodes.index(v2)
        graph[index1][index2] = 1 
        graph[index2][index1] = 1   
        
        # For directed graph i.e, v1 -> v2 means only this code enough
        # graph[index1][index2] = 1
        # For v2 -> v1, it will be 
        # graph[index2][index2] = 1   #Change value if it is a weighted graph
        
        # Assign cost/weight value if it is a weighted graph
        # graph[index1][index2] = cost
        # graph[index2][index1] = cost
    
def deletion(v):
    # For directed, undirected, weighted and unweighted graph
    global node_count
    if v not in nodes:
        print(f"{v} is not present in the graph")
        return
    node_count -= 1
    index_v = nodes.index(v)
    nodes.remove(v)
    graph.pop(index_v)      # Deleting the row in matrix
    for i in graph:         # Deleting the column in matrix
        i.pop(index_v)
    
def delete_edge(v1, v2):
    # For all types of graph.
    # No need to specify the cost because while deleting the edges we need to turn all the cost as 0
    if v1 not in nodes:
        print(f"{v1} is not present in graph...")
    elif v2 not in nodes:
        print(f"{v2} is not present in graph...")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2] = 0
        graph[index2][index1] = 0
    
def _print():
    for i in range(node_count):
        for j in range(node_count):
            print(format(graph[i][j], "<3"), end=" ")       # Format( , "<3") function will give the extra space 
        print()  # For new line
    
    
nodes = []
graph = []
node_count = 0

print("After adding a new node: ")
add("A")
add("B")
add("C")
add("D")
print(nodes)
_print()

print("After adding edges...")
add_edge("A", "B")
add_edge("B", "C")
add_edge("A", "D")
_print()

# print("After removing node...")
# deletion("C")
# _print()

# Output
# After adding a new node: 
# ['A', 'B', 'C', 'D']
# 0   0   0   0   
# 0   0   0   0   
# 0   0   0   0   
# 0   0   0   0   
# After adding edges...
# 0   1   0   1   
# 1   0   1   0   
# 0   1   0   0   
# 1   0   0   0   
# After removing node...
# 0   1   1   
# 1   0   0   
# 1   0   0   

print("After removing the edge...")
delete_edge("B", "C")
_print()

# Output
# After removing the edge...
# 0   1   0   1   
# 1   0   0   0   
# 0   0   0   0   
# 1   0   0   0   