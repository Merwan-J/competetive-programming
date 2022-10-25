class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
#         @cache
#         def dp(i,j):
#             if j == len(word2):
#                 return len(word1)-i
#             if i == len(word1):
#                 return len(word2)-j
            
#             if word1[i] == word2[j]:
#                 return dp(i+1,j+1)
                        
#             return 1 + min(dp(i+1,j),dp(i,j+1),dp(i+1,j+1))
        
#         return dp(0,0)
    
        n = len(word1)
        m = len(word2)
        dp = [[inf]*(m+1) for _ in range(n+1)]
        
        for i in range(n+1):
            dp[i][m] = n-i
        
        for j in range(m+1):
            dp[n][j] = m-j
        
        
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                ans = inf
                if word1[i] == word2[j]:
                    ans = dp[i+1][j+1]
                else:
                    ans = 1 + min(dp[i+1][j],dp[i][j+1],dp[i+1][j+1])
                dp[i][j] = ans
        
        return dp[0][0]