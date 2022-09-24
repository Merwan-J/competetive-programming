class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row,col = len(grid),len(grid[0])
        
#         @cache
#         def dfs(r,c):
#             if r==row or c == col:
#                 return inf
            
#             if r == row - 1 and c == col -1:
#                 return grid[r][c]
            
#             return grid[r][c] + min(dfs(r+1,c),dfs(r,c+1))
        
#         return dfs(0,0)
        
        
        dp = [[inf]*col]*row
        dp[row-1][col-1] = grid[row-1][col-1]
        
        for r in range(row-1,-1,-1):
            for c in range(col-1,-1,-1):
                if r == row-1 and c==col-1:
                    continue
                down,right = inf,inf
                
                if r+1<row:
                    down = dp[r+1][c]
                if c+1<col:
                    right = dp[r][c+1]
                
                dp[r][c] = grid[r][c] + min(down,right)
        
        return dp[0][0]
        