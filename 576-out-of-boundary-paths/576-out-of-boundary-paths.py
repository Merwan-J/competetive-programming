class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        self.count = 0
        memo = {}
        
        def dfs(i,j,move):
            if not(i>-1 and i<m and j>-1 and j<n):
                return 1
            
            if move == 0:
                return 0
            
            if (i,j,move) in memo:
                return memo[(i,j,move)]
            ans = 0
            for a,b in [[0,1],[1,0],[-1,0],[0,-1]]:
                ans = ans + dfs(i+a,j+b,move-1)
            memo[(i,j,move)] = ans
            return ans
        
        
        return dfs(startRow,startColumn,maxMove)%(10**9+7)