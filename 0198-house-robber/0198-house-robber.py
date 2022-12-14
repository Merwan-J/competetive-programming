class Solution:
    def rob(self, nums: List[int]) -> int:
#         rob or don't rob
        
#         if rob: jump one house
#         if not rob: go to the next
            
#         @cache
#         def dp(i):
#             if i >=len(nums):
#                 return 0
            
            # rob = nums[i] + dp(i+2)
            # notrob = dp(i+1)
            
#             return max(rob,notrob)
        
#         return dp(0)
        n = len(nums)
        dp = [0]*(n+1)
        dp[n-1] = nums[n-1]
        
        for i in range(n-2,-1,-1):
            rob = nums[i] + dp[i+2]
            notrob = dp[i+1]
            
            dp[i] = max(rob,notrob)
        
        return dp[0]