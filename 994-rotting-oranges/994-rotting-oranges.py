class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row,col = len(grid),len(grid[0])
        time,fresh = 0,0
        
        rottens = deque([])
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    rottens.append((r,c,0))
                elif grid[r][c] == 1:
                    fresh+=1
                    
        
        def isValid(r,c):
            return not(r == row or r<0 or c == col or c<0)
        
        while rottens:
            r,c,level = rottens.popleft()
            
            for d1,d2 in [(1,0),(0,1),(-1,0),(0,-1)]:
                nr,nc = r+d1,c+d2
                if isValid(nr,nc) and grid[nr][nc] == 1:
                    time = max(time,level+1)
                    grid[nr][nc] = 2
                    rottens.append((nr,nc,level+1))
                    fresh-=1
        
        if fresh>0:
            return -1
        return time
                    
            
            
        
