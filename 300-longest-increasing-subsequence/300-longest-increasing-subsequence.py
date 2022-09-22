class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        n = len(nums)
        dp = [1]*n
        
        for end in range(n):
            for start in range(end):
                if nums[end]>nums[start]:
                    dp[end] = max(1 + dp[start],dp[end])
        
        return max(dp)