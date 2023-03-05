class Solution:
    def jump(self, nums: List[int]) -> int:
        
        
        
        
        @cache
        def dp(i):
            if i >= len(nums)-1:
                return 0
            
            ans = inf
            
            for j in range(1,nums[i]+1):
                ans = min(ans,dp(i+j))
            
            return ans + 1
                
        
        return dp(0)
        
            
                