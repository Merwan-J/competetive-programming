class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        
        @cache
        def dp(r,c):
            if r == m or c == n or grid[r][c] == 1:
                return 0
            
            if r == m-1 and c == n-1:
                return 1
           
            return dp(r+1,c) + dp(r,c+1)
        
        return dp(0,0)
    
        
#         dp = [[0]*n for _ in range(m)]
#         dp[m-1][n-1] = 1 if grid[m-1][n-1]!=1 else 0
        
#         for r in range(m-1,-1,-1):
#             for c in range(n-1,-1,-1):
#                 if grid[r][c] == 1:
#                     continue
#                 if r+1<m:
#                     dp[r][c] += dp[r+1][c]
#                 if c+1<n:
#                     dp[r][c]+=dp[r][c+1]
#         return dp[0][0]
                