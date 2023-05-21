class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        
        
        def dfs(r,c):
            grid[r][c] = 2
            q.append((r,c))
            
            for dr,dc in [(1,0),(0,1),(-1,0),(0,-1)]:
                nr,nc = r+dr,c+dc
                if isvalid(nr,nc) and grid[nr][nc]==1:
                    dfs(nr,nc)
                    
        isvalid = lambda nr,nc: nr<len(grid) and nr>-1 and nc<len(grid) and nc>-1 
        
        q = deque()
        run = True
        
        for r in range(len(grid)):
            for c in range(len(grid)):
                if grid[r][c]==1:
                    dfs(r,c)
                    run = False
                    break
            if not run: break
        
        levels = 0
        while q:
            n = len(q)
            for _ in range(n):
                r,c = q.popleft()
                
                for dr,dc in [(1,0),(0,1),(-1,0),(0,-1)]:
                    nr,nc = r+dr,c+dc
                    
                    if isvalid(nr,nc) and grid[nr][nc] == 0:
                        grid[nr][nc] = 2
                        q.append((nr,nc))
                    elif isvalid(nr,nc) and grid[nr][nc] == 1:
                        return levels
            levels+=1
        return levels
                
                    
        
                