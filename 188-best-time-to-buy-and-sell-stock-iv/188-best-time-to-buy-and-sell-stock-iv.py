class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        
        @cache
        def dp(i,buy,k):
            if k==0 or i==len(prices):
                return 0
            
            ans = dp(i+1,buy,k)
            if buy:
                ans = max(ans,-prices[i] + dp(i+1,False, k))
            else:
                ans = max(ans,prices[i] + dp(i,True,k-1))
            return ans
        
        return dp(0,True,k)
            