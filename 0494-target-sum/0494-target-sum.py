class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
#         @cache
#         def dp(i,total):
#             if i == 0:
#                 ans = 0
#                 if total+nums[i] == target: ans+=1
#                 if total-nums[i] == target: ans+=1
#                 return ans
            
#             add = dp(i-1,total+nums[i])
#             subtract = dp(i-1,total-nums[i])
            
#             return add + subtract
        
        
#         return dp(len(nums)-1,0)
    
        dp = [[0]*2001 for _ in range(len(nums))]
        
        dp[0][nums[0]] = 1
        dp[0][-nums[0]%2001] += 1
        
        for i in range(1,len(nums)):
            for cur in range(-1000,1001):
                add = dp[i-1][(cur + nums[i])%2001]
                subtract = dp[i-1][(cur-nums[i])%2001]
                
                dp[i][cur%2001] = add + subtract
        
        return dp[len(nums)-1][target]
        
    
        
        