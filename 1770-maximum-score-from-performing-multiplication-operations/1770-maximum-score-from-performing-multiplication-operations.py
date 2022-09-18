class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        m = len(multipliers)
        n = len(nums)
        dp = [[0]*(m+1) for _ in range(m+1)]
        
        for opp in range(m-1,-1,-1):
            for left in range(opp+1):
                pickleft = nums[left]*multipliers[opp] + dp[opp+1][left+1]
                pickright = nums[n-1-(opp-left)]*multipliers[opp] + dp[opp+1][left]
                dp[opp][left] = max(pickleft,pickright)
        
        return dp[0][0]
                