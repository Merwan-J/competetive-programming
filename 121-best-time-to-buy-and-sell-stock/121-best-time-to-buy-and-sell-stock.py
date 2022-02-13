class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxDiff = 0
        
        # for i in range(len(prices)):
        #     for j in range(i+1,len(prices)):
        #         if prices[i]<prices[j]:
        #             maxDiff = max(maxDiff,prices[j]-prices[i])
                    
        l,r  = 0,1
        while r<len(prices):
            if prices[l]>prices[r]:
                l = r
                r = l+1
            else:
                maxDiff = max(maxDiff,prices[r]-prices[l])
                r+=1
        
        return maxDiff