import heapq

heaplist = []
print(heaplist)

def heap():
    #Converting the normal list in to heap structure
    heapq.heapify(heaplist)
    print(heaplist)

    # pushing the new node to heap
    heapq.heappush(heaplist, 50)
    print(heaplist)

    # Removing the node from heap
    heapq.heappop(heaplist)
    print(heaplist)

    # Removing and adding the node at the same time
    heapq.heappushpop(heaplist, 80)
    print(heaplist)

usr = [4,66,5,8,14,35,21,9,]
for i in usr:
    heaplist.append(i)
    
heap()

# Output
# [4, 8, 5, 9, 14, 35, 21, 66]
# [4, 8, 5, 9, 14, 35, 21, 66, 50]
# [5, 8, 21, 9, 14, 35, 50, 66]
# [8, 9, 21, 66, 14, 35, 50, 80]