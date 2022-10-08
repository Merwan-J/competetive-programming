class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row,col = len(grid),len(grid[0])
        count = 0
        
        
        def dfs(r,c):
            if r<0 or c<0 or c == col or r == row or grid[r][c] == 0:
                return 1
            if grid[r][c] == -1:
                return 0
            
            grid[r][c] = -1
            ans = 0
            for dr,dc in [(1,0),(0,-1),(-1,0),(0,1)]:
                ans+=dfs(r+dr,c+dc)
            
            return ans
                            
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    return dfs(r,c)
