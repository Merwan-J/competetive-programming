#User function Template for python3
from heapq import heappop,heappush
class Solution:
        
    def MinimumEffort(self, grid):
        #code here
        row,col = len(grid),len(grid[0])
        
        ans = [[float("inf")]*col for _ in range(row)]
        ans[0][0] = 0
        q = [(0,0,0)]
        
        
        while q:
            diff,r,c = heappop(q)
            
            if (r,c) == (row-1,col-1):
                break
            
            for dr,dc in [(1,0),(0,1),(-1,0),(0,-1)]:
                nr,nc = r+dr,c+dc
                if nr>=0 and nr<row and nc>=0 and nc<col:
                    curdiff = max(ans[r][c],abs(grid[r][c]-grid[nr][nc]))
                    if curdiff <ans[nr][nc]:
                        ans[nr][nc] = curdiff
                        heappush(q,(curdiff,nr,nc))
        
        return ans[row-1][col-1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n,m=map(int,input().split())
        a=[]
        for i in range(n):
            li=list(map(int,input().split()))
            a.append(li)
        ob = Solution()
        ans = ob.MinimumEffort(a)
        print(ans)
        tc -= 1
# } Driver Code Ends