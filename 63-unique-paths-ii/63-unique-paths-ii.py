class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
#         Top down approach

#         dp = {}
        
#         def dfs(row,col):
#             if row>=len(grid) or col>=len(grid[0]) or grid[row][col]==1:
#                 return 0
            
#             if row==len(grid)-1 and col == len(grid[0])-1:
#                 return 1
#             if (row,col) in dp:
#                 return dp[(row,col)]
            
#             dp[(row,col)] = dfs(row+1,col) + dfs(row,col+1)
            
#             return dp[(row,col)]
        
#         return dfs(0,0)


#  Bottom up approach
        row = len(grid)
        col = len(grid[0])
        result = [[0]*(col+1) for i in range(row+1)]
        result[row][col-1] = 1
        
        for r in range(row-1,-1,-1):
            for c in range(col-1,-1,-1):
                if grid[r][c] == 0:
                    result[r][c] = result[r+1][c] + result[r][c+1]
                
        return result[0][0]
        