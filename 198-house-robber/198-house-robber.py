class Solution:
    def rob(self, nums: List[int]) -> int:
#         bottom up
        n = len(nums)
        dp = [0]*(n+2)
        
        for i in range(2,n+2):
            dp[i] = max(dp[i-1],dp[i-2]+nums[i-2])
        
        return dp[-1]
        
#         top down
    
        n = len(nums)
        memo = [0]*(n)
        
        def helper(n):
            if memo[n] is not None:
                return memo[n]
            if n<0:
                return 0
            memo[n] = max(helper(n-1),helper(n-2)+nums[n-1])
            
            return memo[n]
        return helper(n)