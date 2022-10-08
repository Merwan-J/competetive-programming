class Solution:
    def colorBorder(self, grid: List[List[int]], x: int, y: int, color: int) -> List[List[int]]:
        
        row,col = len(grid),len(grid[0])
        visited = set()
        ans = []
        def dfs(r,c,old):
            if (r,c) in visited:
                return 
            
            visited.add((r,c))
            
            for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr,nc = r+dr,c+dc
                if nr<0 or nc<0 or nc == col or nr == row or grid[nr][nc]!=old:
                    ans.append((r,c))
                else:
                    dfs(nr,nc,old)
                    
        dfs(x,y,grid[x][y])
        
        for r,c in ans:
            grid[r][c] = color
        
        return grid