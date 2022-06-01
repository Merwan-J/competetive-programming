class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = dict()
        
        def getProfit(i,buying):
            
            if i>=len(prices):
                return 0
            
            if (i,buying) in dp:
                return dp[(i,buying)]
            
            skip = getProfit(i+1,buying)
            if buying:
                buy = getProfit(i+1,not buying) - prices[i]
                dp[(i,buying)] = max(skip,buy)
            else:
                sell = getProfit(i+1,not buying) + prices[i]
                dp[(i,buying)] = max(skip,sell)
            return dp[(i,buying)]
        
        return getProfit(0,True)