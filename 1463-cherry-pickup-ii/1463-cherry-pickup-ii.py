class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        row,col = len(grid),len(grid[0])
        
#         @cache
#         def dfs(r,c1,c2):
#             if r == row or c1<0 or c1>=col or c2<0 or c2>=col:
#                 return 0
            
#             ans = 0
#             for a in range(-1,2):
#                 for b in range(-1,2):
#                     ans = max(ans,dfs(r+1,c1+a,c2+b))
            
#             if c1 == c2:
#                 ans-=grid[r][c1]
            
#             return ans + grid[r][c1] + grid[r][c2]
        
        
#         return dfs(0,0,col-1)
    
        
        
        dp = [[[0]*col for _ in range(col)] for i in range(row+1)]
        
        for r in range(row-1,-1,-1):
            for c1 in range(col):
                for c2 in range(col):
                    ans = 0
                    for a in range(-1,2):
                        for b in range(-1,2):
                            if c1+a>=0 and c1+a<col and c2+b>=0 and c2+b<col:
                                ans = max(ans,dp[r+1][c1+a][c2+b])
                    if c1 == c2:
                        ans-=grid[r][c1]
                    
                    dp[r][c1][c2] = ans + grid[r][c1] + grid[r][c2]
                
        return dp[0][0][col-1]
                                
            