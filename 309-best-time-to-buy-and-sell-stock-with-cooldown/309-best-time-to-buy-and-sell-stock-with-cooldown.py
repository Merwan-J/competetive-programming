class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = dict()
        
        def getProfit(i,buy):
            if i >= len(prices):
                return 0
            
            if (i,buy) in memo:
                return memo[(i,buy)]
            
            cooldown = getProfit(i+1,buy)
            
            if buy:
                buyy = getProfit(i+1,not buy) - prices[i]
                memo[(i,buy)] = max(cooldown,buyy)
                
            else:
                sell = prices[i] + getProfit(i+2, not buy)
                memo[(i,buy)] = max(cooldown,sell)
            
            return memo[(i,buy)]
        
        return getProfit(0,True)
    
    
            
            
            