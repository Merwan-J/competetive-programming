class Solution:
    def rob(self, nums: List[int]) -> int:
#         memo = {}
#         def helper(i):
#             if i == 0:
#                 return nums[i]
#             if i == 1:
#                 return max(nums[i],nums[0])
#             if i in memo:
#                 return memo[i]
            
#             memo[i] = max(helper(i-1),helper(i-2)+nums[i])
            
#             return memo[i]
        
#         return helper(len(nums)-1)
    
        dp = [0]*(len(nums))
        dp[0] = nums[0]
        if len(nums)>1:
            dp[1] = max(dp[0],nums[1])
        
        for i in range(2,len(dp)):
            dp[i] = max(dp[i-1],dp[i-2]+nums[i])
        
        return dp[-1]