class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        
        if len(grid)==1:
            return grid[0][0]
        
#         @cache
#         def dfs(row,col):
#             if row == len(grid):
#                 return 0
            
#             ans = inf
#             for i in range(len(grid[0])):
#                 if i!=col:
#                     ans = min(ans,dfs(row+1,i))
            
#             return ans + grid[row][col]
        
#         ans = inf
#         for col in range(len(grid[0])):
#             ans = min(ans,dfs(0,col))
        
#         return ans
        def find_two_smallest(a):
            m1, m2 = float('inf'), float('inf')
            for i, x in enumerate(a):
                if x <= m1:
                    m1, m2, i1 = x, m1, i
                elif x < m2:
                    m2 = x
            return [m1, m2, i1]
        
        row = len(grid)
        col = len(grid[0])
        
        dp = [0]*col 
        small = [0,0,0]
        
        for r in range(row-1,-1,-1):
            for c in range(col):
                shift = small[0] if small[2]!=c else small[1]
                dp[c] = grid[r][c] + shift
            small = find_two_smallest(dp)
            
        return small[0] 
        