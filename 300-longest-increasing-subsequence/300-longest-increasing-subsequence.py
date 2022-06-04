class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
#         Bottom up approach

#         n = len(nums)
#         dp = [1]*n
        
#         for i in range(n-2,-1,-1):
#             cur = nums[i]
#             for j in range(i+1,n):
#                 if cur<nums[j]:
#                     dp[i] = max(dp[i],dp[j]+1)
        
#         return max(dp)
    

# Top down approach
        dp = {}
        
        def dfs(i):
            if i in dp:
                return dp[i]
                        
            dp[i] = 1
            
            for j in range(i+1,len(nums)):
                if nums[j]>nums[i]:
                    dp[i] = max(dp[i],dfs(j)+1)
            
            return dp[i]
        
        ans = 1
        for i in range(len(nums)):
            ans = max(dfs(i),ans)

        return ans