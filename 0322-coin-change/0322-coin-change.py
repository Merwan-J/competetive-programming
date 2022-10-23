class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        
        @cache
        def dp(target):
            if target == 0:
                return 0
            if target<0:
                return inf
            
            ans = inf
            
            for coin in coins:
                ans = min(ans,1 + dp(target-coin))
            
            return ans
        
        ans = dp(amount)
        
        return -1 if ans == inf else ans
    