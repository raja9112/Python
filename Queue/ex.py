#User function Template for python3

class Solution:
    
    #Function to find maximum of each subarray of size k.
    def max_of_subarrays(self,arr,n,k):
        
        q = deque()
        i = 0
        result = []
        #removing out of range of k
        while i<n:
            if not len(q)==0 and q[0] <= i-k:
                q.popleft()
            #removing smaller elements in k range
            while not len(q)==0 and arr[q[-1]] < arr[i]:
                q.pop()
            q.append(i)
            if i>=k-1:
                result.append(arr[q[0]])
            i+=1
        return result



        
