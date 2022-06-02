class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
            # Bottom UP Approach
#         dp = {}
        
#         def dfs(row,col):
#             if (row==len(grid) and col==len(grid[0])-1) or(row==len(grid)-1 and col==len(grid[0])):
#                 return 0
#             if row>=len(grid) or col>=len(grid[0]):
#                 return float('inf')
            
#             if (row,col) in dp:
#                 return dp[(row,col)]
            
#             dp[(row,col)] = grid[row][col] + min(dfs(row+1,col),dfs(row,col+1))
            
#             return dp[(row,col)]
        
#         return dfs(0,0)



#           Top down approach


        row = len(grid)
        col = len(grid[0])
        result = [[float('inf')]*(col+1) for j in range(row+1)]
        result[row-1][col] = 0
        
        for r in range(row-1,-1,-1):
            for c in range(col-1,-1,-1):
                result[r][c] = grid[r][c] + min(result[r+1][c],result[r][c+1])
        
        return result[0][0]
