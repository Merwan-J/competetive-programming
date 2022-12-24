class Solution:
    def numTilings(self, n: int) -> int:
        
        
#         @cache
#         def dp(i,state):
#             if i == n:
#                 return 1
            
#             ans = 0
#             isNextFree = i+1<n
            
#             if state == 0:
#                 ans+=dp(i+1,0)
#                 if isNextFree:
#                     ans+= dp(i+1,3) + dp(i+1,1) + dp(i+1,2)
#             elif state == 1 and isNextFree:
#                 ans+=dp(i+1,3) + dp(i+1,2)                
#             elif state == 2 and isNextFree:
#                 ans += dp(i+1,3) + dp(i+1,1)
#             elif state == 3:
#                 ans += dp(i+1,0)
            
#             return ans
        
#         return dp(0,0)%(10**9+7)
    
    
        dp = [[0]*4 for _ in range(n+1)] 
        dp[n] = [1,1,1,1]
        
        for i in range(n-1,-1,-1):
            for state in range(4):
                
                ans = 0
                isNextFree = i+1<n

                if state == 0:
                    ans+=dp[i+1][0]
                    if isNextFree:
                        ans+= dp[i+1][3] + dp[i+1][1] + dp[i+1][2]
                elif state == 1 and isNextFree:
                    ans+=dp[i+1][3] + dp[i+1][2]                
                elif state == 2 and isNextFree:
                    ans += dp[i+1][3] + dp[i+1][1]
                elif state == 3:
                    ans += dp[i+1][0]
                
                dp[i][state] = ans
        
        return dp[0][0]%(10**9+7)
                