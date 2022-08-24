class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.target = target
        
        @cache
        def dp(i,amount):
            
            if i == len(nums) and amount == self.target:
                return 1
            elif i == len(nums) and amount != self.target:
                return 0
            
            return dp(i+1,amount-nums[i]) + dp(i+1,amount+nums[i])
        
        
        return dp(0,0)
    
            