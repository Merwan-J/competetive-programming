class Solution:  
    def rob(self, nums: List[int]) -> int:
        if len(nums)<3:
            return max(nums)
        def compute(arr):
            dp = [0]*len(arr)
            dp[0] = arr[0]
            dp[1] = max(arr[1],dp[0])

            for i in range(2,len(arr)):
                dp[i] = max(dp[i-1],dp[i-2]+arr[i])

            return dp[-1]
        return max(compute(nums[1:]),compute(nums[:-1]))