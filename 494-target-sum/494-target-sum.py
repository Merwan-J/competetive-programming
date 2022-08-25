class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
#         self.target = target
        
#         @cache
#         def dp(i,amount):
            
#             if i == len(nums) and amount == self.target:
#                 return 1
#             elif i == len(nums) and amount != self.target:
#                 return 0
            
#             return dp(i+1,amount-nums[i]) + dp(i+1,amount+nums[i])
        
        
#         return dp(0,0)
        
        dp = [[0]*2001 for _ in range(len(nums))]
        dp[0][nums[0]] = 1
        dp[0][-nums[0]] += 1
        
        for i in range(1,len(nums)):
            num = nums[i]
            for amount in range(-1000,1001):
                dp[i][amount+num] += dp[i-1][amount]
                dp[i][amount-num] += dp[i-1][amount] 
        
        for i in range(len(dp[-1])):
            if dp[-1][i]!=0:
                print(i,dp[-1][i])
        return dp[-1][target]
            