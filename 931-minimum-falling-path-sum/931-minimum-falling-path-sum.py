class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        row = len(matrix)
        col = len(matrix[0])

#         @cache
#         def dfs(r,c):
#             if r == row:
#                 return 0
#             if c==-1 or c==col:
#                 return inf
            
#             return matrix[r][c] + min(dfs(r+1,c),dfs(r+1,c+1),dfs(r+1,c-1))
        
#         ans = inf
        
#         for i in range(col):
#             ans = min(dfs(0,i),ans)
        
#         return ans

        dp = matrix[-1][:]
        
        for r in range(row-2,-1,-1):
            prev = dp.copy()
            for c in range(col):
                
                down,downleft,downright = inf,inf,inf
                
                if c+1<row:
                    downright = prev[c+1]
                if c-1>-1:
                    downleft = prev[c-1]
                down = prev[c]
                
                dp[c] = matrix[r][c] + min(down,downright,downleft)
                
        return min(dp)