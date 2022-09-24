class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
#         @cache
#         def dfs(row,col):
#             if row == len(triangle):
#                 return 0
            
#             return triangle[row][col] + min(dfs(row+1,col),dfs(row+1,col+1))
        
#         return dfs(0,0)
            
        dp = triangle[-1][:]
        
        for row in range(len(dp)-2,-1,-1):
            for col in range(row+1):
                dp[col] = triangle[row][col] + min(dp[col],dp[col+1])
        return dp[0]