#Example using heapify from heapq module.

import heapq

li=[3,6,7,5,4,1]

heapq.heapify(li)

add=int(input("Enter the element you wish to: "))
heapq.heappush(li,add)

print(list(li))

print(heapq.nlargest(3,li))
print(heapq.nsmallest(3,li))