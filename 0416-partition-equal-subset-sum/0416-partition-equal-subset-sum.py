class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        n = len(nums)
        
        if total - total//2 != total//2:
            return False
        
        total = total//2
        dp = [[False]*(total+1) for row in range(n)]
        
        for r in range(n):
            dp[r][0] = True
        
        if nums[0]<=total:
            dp[0][nums[0]] = True
        
        for i in range(1,n):
            for target in range(total+1):
                not_pick = dp[i-1][target]
                pick = False
                if target>=nums[i]:
                    pick = dp[i-1][target-nums[i]]
                dp[i][target] = pick or not_pick
        
        return dp[n-1][total]