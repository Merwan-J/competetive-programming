class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        row,col = len(grid),len(grid[0])
        
        @cache
        def dfs(r1,c1,r2,c2):
            if r1>=row or r2>=row or c1<0 or c1>=col or c2<0 or c2>=col:
                return -inf
            
            if grid[r1][c1] == -1 or grid[r2][c2]==-1:
                return -inf
            
            if c1 == c2 == r1 == r2 == row-1:
                return grid[r1][c1]
            
            ans = grid[r1][c1] + grid[r2][c2] 
            if r1==r2 and c1==c2:
                ans-=grid[r1][c1]
            
            return ans + max(
                            dfs(r1,c1+1,r2,c2+1),dfs(r1,c1+1,r2+1,c2),
                            dfs(r1+1,c1,r2,c2+1),dfs(r1+1,c1,r2+1,c2)
                            )
        
        ans = dfs(0,0,0,0)
        return 0 if ans == -inf else ans