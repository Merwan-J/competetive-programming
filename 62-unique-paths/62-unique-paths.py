class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
#         Top Down approach
#         memo = {}
        
#         def dfs(row,col):
#             if row==m-1 and col ==n-1:
#                 return 1
            
#             if row>=m or col>=n:
#                 return 0
#             if (row,col) in memo:
#                 return memo[(row,col)]
#             memo[(row,col)] = dfs(row+1,col) + dfs(row,col+1)
            
#             return memo[(row,col)]
            
            
#         return dfs(0,0)
    
    
    
# Bottom Up approach

        grid = [[0]*(n+1) for i in range(m+1)]
        grid[m-1][n] = 1
        
        for r in range(m-1,-1,-1):
            for c in range(n-1,-1,-1):
                grid[r][c] = grid[r+1][c] + grid[r][c+1]
        return grid[0][0]