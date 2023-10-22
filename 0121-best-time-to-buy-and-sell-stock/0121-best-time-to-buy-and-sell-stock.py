class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]
        
        for sell in prices:
            profit = max(profit,sell-buy)
            
            if sell<buy:
                buy = sell
        
        return profit
    
    