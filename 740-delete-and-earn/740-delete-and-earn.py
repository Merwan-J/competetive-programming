class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        dp = [0]*(max(nums)+1)
        dp[1] = counter[1]
        
        for num in range(2,len(dp)):
            dp[num] = max(dp[num-1],dp[num-2]+counter[num]*num)
        
        return dp[-1]
        
        
        
#         counter = collections.Counter(nums)
#         @cache
#         def maxPoints(num):
#             if num == 0:
#                 return 0
#             if num == 1:
#                 return counter[1]
            
#             return max(counter[num]*num+maxPoints(num-2),maxPoints(num-1))
        
#         return maxPoints(max(nums))
        
        
#         counter = collections.Counter(nums)
#         nums = sorted(list(set(nums)))
#         memo = {}

#         @cache
#         def helper(i,deleted,):
#             if i >= len(nums):
#                 return 0
         
#             dontPick = helper(i+1,False)
#             pick = counter[nums[i]]*nums[i] + helper(i+1,True) if not(deleted and nums[i-1]+1==nums[i]) else 0
            
#             return max(dontPick,pick)
        
#         return helper(0,False)