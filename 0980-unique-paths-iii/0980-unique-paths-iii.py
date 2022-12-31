class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        empty = 0
        dead = 0
        start = None
        end = None
        
        m = len(grid)
        n = len(grid[0])
        
        for r in range(m):
            for c in range(n):
                cur = grid[r][c]
                
                if cur == 0:
                    empty+=1
                elif cur == 1:
                    start = (r,c)
                    
        
        def dfs(r,c,visited):
            if r<0 or r>=m or c<0 or c>=n or grid[r][c] == -1 or (r,c) in visited:
                return 0
            if grid[r][c] == 2:
                return 1 if len(visited) == empty + 1 else 0
            
            visited.add((r,c))
            
            ans = dfs(r,c+1,visited)+dfs(r,c-1,visited)+dfs(r+1,c,visited)+dfs(r-1,c,visited)
            visited.remove((r,c))
            
            return ans

        return dfs(start[0],start[1],set())
            
            
        