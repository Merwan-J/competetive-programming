class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r,c):
            if r<0 or r==len(grid) or c<0 or c==len(grid[0]) or grid[r][c]=="0":
                return
            grid[r][c] = "0"
            for d1,d2 in [(-1,0),(1,0),(0,-1),(0,1)]:
                dfs(r+d1,c+d2)
            
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    dfs(r,c)
                    count+=1
        
        return count