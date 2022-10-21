class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        self.found = False
        
        @cache
        def dp(i,cur):
            nonlocal total
            if total-cur == cur or self.found:
                self.found = True
                return True
            if i == len(nums) or total-cur<cur:
                return False
            
            return dp(i+1,cur+nums[i]) or dp(i+1,cur)
        
        return dp(0,0)