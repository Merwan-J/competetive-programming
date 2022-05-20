class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def explore(row,col):
            if row>=0 and col>=0 and row<len(grid) and col<len(grid[0]) and grid[row][col] == '1':
                grid[row][col] = '0'
                
                explore(row+1,col)
                explore(row-1,col)                
                explore(row,col+1)                
                explore(row,col-1)
        
        islands = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    explore(row,col)
                    islands += 1
        
        return islands