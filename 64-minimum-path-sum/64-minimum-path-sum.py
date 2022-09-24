class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row,col = len(grid),len(grid[0])
        
        @cache
        def dfs(r,c):
            if r==row or c == col:
                return inf
            
            if r == row - 1 and c == col -1:
                return grid[r][c]
            
            return grid[r][c] + min(dfs(r+1,c),dfs(r,c+1))
        
        return dfs(0,0)