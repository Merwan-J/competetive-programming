class Solution:
    def findFarmland(self, grid: List[List[int]]) -> List[List[int]]:
        
        def dfs(r,c):
            if r<0 or r==len(grid) or c<0 or c==len(grid[0]) or grid[r][c]==0:
                return (-1,-1)
            
            grid[r][c] = 0
            sr,sc = r,c
            for d1,d2 in [(-1,0),(1,0),(0,-1),(0,1)]:
                coord = dfs(r+d1,c+d2)
                sr = max(coord[0],sr)
                sc = max(coord[1],sc)
            
            return sr,sc
    
        ans = []    
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    br,bc = dfs(r,c)
                    ans.append([r,c,br,bc])
        
        return ans