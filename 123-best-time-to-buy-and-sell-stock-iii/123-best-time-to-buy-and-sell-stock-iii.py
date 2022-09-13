class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @lru_cache(maxsize=None)
        def dp(i, t, bought):
            if i >= len(prices) or t == 0:
                return 0
            profit = dp(i + 1, t, bought);
            if bought:
                profit = max(profit, dp(i + 1, t - 1, not bought) + prices[i])
            else:
                profit = max(profit, dp(i + 1, t, not bought) - prices[i])
            return profit
        
        return dp(0, 2, False)