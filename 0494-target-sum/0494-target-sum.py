class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        @cache
        def dp(i,total):
            if i == 0:
                ans = 0
                if total+nums[i] == target: ans+=1
                if total-nums[i] == target: ans+=1
                return ans
            
            add = dp(i-1,total+nums[i])
            subtract = dp(i-1,total-nums[i])
            
            return add + subtract
        
        
        return dp(len(nums)-1,0)