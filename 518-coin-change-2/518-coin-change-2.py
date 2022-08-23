class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        @cache
        def dp(i,target):
            if target == 0:
                return 1
            if target<0:
                return 0
            
            ans = 0
            for idx in range(i,len(coins)):
                if target>=coins[idx]:
                    ans += dp(idx,target-coins[idx])
            
            return ans
        
        return dp(0,amount)
            
        
        