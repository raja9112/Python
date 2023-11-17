#Program to find minimum cost of ropes

"""Input:
n = 4
arr[] = {4, 3, 2, 6}
Output: 
29
Explanation:
We can connect the ropes in following ways.
1) First connect ropes of lengths 2 and 3.
Which makes the array {4, 5, 6}. Cost of
this operation 2+3 = 5. 
2) Now connect ropes of lengths 4 and 5.
Which makes the array {9, 6}. Cost of
this operation 4+5 = 9.
3) Finally connect the two ropes and all
ropes have connected. Cost of this 
operation 9+6 =15
Total cost for connecting all ropes is 5
+ 9 + 15 = 29."""


import heapq

class solution():
     def minCost(self,arr,n):
        if n == 0:
            return arr[0]
        
        heapq.heapify(arr)

        cost=0

        while len(arr)>1:
            a=heapq.heappop(arr)
            b=heapq.heappop(arr)
            temp=a+b
            cost+=temp
            heapq.heappush(arr, temp)

        return cost

n=int(input("How many numbers do you want to add: "))
arr=[]
for i in range(n):
    arr.append(int(input("Enter the number: ")))

obj=solution()
print(obj.minCost(arr, n))