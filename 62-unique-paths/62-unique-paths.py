class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        @cache
        def dp(r,c):
            if r==m or c==n:
                return 0
            if r == m-1 and c == n-1:
                return 1
            
            return dp(r+1,c) + dp(r,c+1)
        
        return dp(0,0)
        
#         
        # r x c m x n
        
#         basecase= dp[m-1][n-1] = 1
#         return dp[0][0]
        
#         dp[r+1][c] + dp[r][c+1]
        
#         r = m-1 -> 0
#         c = n-1 -> 0

        dp = [[0]*n for _ in range(m)]
        dp[m-1][n-1] = 1
        
        for r in range(m-1,-1,-1):
            for c in range(n-1,-1,-1):                
                if c+1<n:
                    dp[r][c] += dp[r][c+1]
                if r+1<m:
                    dp[r][c] += dp[r+1][c]                
        
        return dp[0][0]
    