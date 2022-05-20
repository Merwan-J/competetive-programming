class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def explore(row,col):
            if row>=0 and col>=0 and row<len(grid) and col<len(grid[0]) and grid[row][col]==1:
                grid[row][col] = 0
                
                explore(row+1,col)
                explore(row-1,col)
                explore(row,col+1)
                explore(row,col-1)
        
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if row in [0,len(grid)-1] or col in [0,len(grid[0])-1]:
                    explore(row,col)
                             
        count = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]==1:
                    count+= 1
        
        return count