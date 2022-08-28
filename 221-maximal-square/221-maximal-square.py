class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        h,w = len(matrix),len(matrix[0])
        
#         dp = [[0]*w for _ in range(h)]
#         ans = 0
        
#         for row in range(h):
#             for col in range(w):
#                 dp[row][col] = int(matrix[row][col])
#                 if dp[row][col] == 1 and row>0 and col>0:
#                     dp[row][col] += min(dp[row-1][col],dp[row][col-1],dp[row-1][col-1])
#                 ans = max(ans,dp[row][col])
        
#         return ans * ans
    
        self.ans = 0    
        @cache
        def dp(row,col):
            if row>=len(matrix) or col>=len(matrix[0]):
                return 0
            ans = 1 + min(dp(row+1,col),dp(row,col+1),dp(row+1,col+1))
            if matrix[row][col] == "0":
                return 0
            
            self.ans = max(self.ans,ans)

            
            return ans
        
        dp(0,0)
        return self.ans**2
            
            
            
        
        