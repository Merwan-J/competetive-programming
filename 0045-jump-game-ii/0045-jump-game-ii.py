class Solution:
    def jump(self, nums: List[int]) -> int:
        
        
        
        
#         @cache
#         def dp(i):
#             if i >= len(nums)-1:
#                 return 0
            
#             ans = inf
            
#             for j in range(1,nums[i]+1):
#                 ans = min(ans,dp(i+j))
            
#             return ans + 1
                
        
#         return dp(0)
        
        
        n = len(nums)
        dp = [inf] * n
        dp[n-1] = 0
        
        for i in range(n-2,-1,-1):
            for j in range(1,nums[i]+1):
                if i+j>=n: break
                dp[i] = min(dp[i],dp[i+j] + 1)
        
        return dp[0]
        
                