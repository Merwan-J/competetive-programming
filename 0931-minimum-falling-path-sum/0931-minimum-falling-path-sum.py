class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
#         def dp(r,c):
#             if r==len(matrix):
#                 return 0
            
#             ans = inf
            
#             for i in [0,1,-1]:
#                 if -1<c+1<len(matrix[0]):
#                     ans = min(ans,dp(r+1,c+i))
            
#             return ans + matrix[r][c]
        
        
#         ans = inf
#         for c in range(len(matrix[0])):
#             ans = min(ans,dp(0,c))
        
#         return ans
    
        n = len(matrix)
        dp = [[0]*n for _ in range(n+1)]
        
        for r in range(n-1,-1,-1):
            for c in range(n):
                ans = inf
                for i in [0,1,-1]:
                    if -1<c+i<len(matrix[0]):
                        ans = min(ans,dp[r+1][c+i])
                dp[r][c] = ans + matrix[r][c]

        return min(dp[0])