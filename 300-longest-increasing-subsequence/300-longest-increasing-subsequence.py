class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1]*n
        
        for i in range(n-2,-1,-1):
            cur = nums[i]
            for j in range(i+1,n):
                if cur<nums[j]:
                    dp[i] = max(dp[i],dp[j]+1)
        
        return max(dp)