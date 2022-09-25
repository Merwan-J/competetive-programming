class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        
        if len(grid)==1:
            return grid[0][0]
        
#         @cache
#         def dfs(row,col):
#             if row == len(grid):
#                 return 0
            
#             ans = inf
#             for i in range(len(grid[0])):
#                 if i!=col:
#                     ans = min(ans,dfs(row+1,i))
            
#             return ans + grid[row][col]
        
#         ans = inf
#         for col in range(len(grid[0])):
#             ans = min(ans,dfs(0,col))
        
#         return ans

        row = len(grid)
        col = len(grid[0])
        
        dp = [0]*col
        
        for r in range(row-1,-1,-1):
            cur = []
            for c in range(col):
                cur.append(grid[r][c] + dp[c])
            
            lmin = [inf]*col
            rmin = [inf]*col
            
            for i in range(1,col):
                lmin[i] = min(cur[i-1],lmin[i-1])
            
            for i in range(col-2,-1,-1):
                rmin[i] = min(cur[i+1],rmin[i+1])
            
            for i in range(col):
                dp[i] = min(rmin[i],lmin[i])
                
        return min(dp)
        