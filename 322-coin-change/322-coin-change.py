class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        @cache
        def dp(total):
            if total == 0:
                return 0
            if total <0:
                return float('inf')
            
            return 1 + min(dp(total-coin) for coin in coins)
        
        ans = dp(amount)
        return -1 if ans == float('inf') else ans
    