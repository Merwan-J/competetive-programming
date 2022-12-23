class Solution:
    def maxProfit(self, prices: List[int]) -> int:
#         two states:
#             Buying 
#             Selling
            
#         will use the variable canBuy to know on which state we are
#         will use i to know which day we are on
        
#         can buy only if is on buying state
#         can seel only if it is on buying state
        
#         has two choices to make at each day if it is on buying state
#             buy or not buy
        
#         has two choices to make at each if it is on selling state
#             to sell or not sell
            
#         if it has sold then it should jump the next day
        
#         recursively find the maximum profit this way
#         base case out of bound: return profit of 0

        
        
        # check if out of bound
        # check which state we are on
        # if buying state: the max is going to be buy today
        @cache
        def dp(i,isBuying):
            if i>=len(prices):
                return 0
            
            ans = dp(i+1,isBuying)
            
            if isBuying:
                ans = max(ans,dp(i+1,not isBuying)-prices[i])
            else:
                ans = max(ans,prices[i] + dp(i+2,not isBuying))
            
            return ans
        
        return dp(0,True)
        
        
            