class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        
        @cache
        def dp(i,target):
            if target == 0:
                return 0
            
            if i == 0:
                return target//coins[i] if target%coins[i] == 0 else inf
            
            not_pick = dp(i-1,target)
            pick = inf
            
            if target-coins[i]>-1:
                pick = 1 + dp(i,target-coins[i])
            
            return min(not_pick,pick)
        
        ans = dp(len(coins)-1,amount)
        
        return -1 if ans == inf else ans
        
        
        