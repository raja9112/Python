from collections import deque

class Solution:
    def RottenOrange(self, arr):

        if not arr:
            return 0

        q=deque()

        row=len(arr)
        col=len(arr[0])

        fresh_oranges=0

        for i in range(row):
            for j in range(col):
                if arr[i][j]==1:
                    fresh_oranges+=1
                elif arr[i][j]==2:
                    q.append((i,j,0))

        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        minutes=0

        while q:
            i,j,minutes=q.popleft()

            for di,dj in directions:
                ni,nj= i+di, j+dj

                if 0<= ni < row and 0<=nj<col and arr[ni][nj]==1:
                    arr[ni][nj]=2
                    fresh_oranges-=1
                    q.append((ni,nj,minutes+1))

        if fresh_oranges == 0:
            return minutes
        else:
            return -1

grid = [
    [0,1,2],
    [0,1,2],
    [2, 1, 1]
]

solution = Solution()
result = solution.RottenOrange(grid)
print("Minutes to rot all oranges:", result)