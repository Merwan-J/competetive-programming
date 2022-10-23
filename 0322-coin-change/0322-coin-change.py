class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        
#         @cache
#         def dp(target):
#             if target == 0:
#                 return 0
            
#             ans = inf
            
#             for coin in coins:
#                 if target<0:
#                     ans = min(ans,1 + dp(target-coin))
            
#             return ans
        
#         ans = dp(amount)
        
#         return -1 if ans == inf else ans
        
        dp = [inf]*(amount+1)
        dp[0] = 0
        
        for cur in range(1,amount+1):
            for coin in coins:
                if cur-coin>=0:
                    dp[cur] = min(dp[cur],dp[cur-coin] + 1)
        
        return -1 if dp[amount] == inf else dp[amount]
        