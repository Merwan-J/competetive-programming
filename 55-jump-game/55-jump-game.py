class Solution:
    def canJump(self, nums: List[int]) -> bool:
        k = nums[0]
        
        for i in range(1,len(nums)):
            k-=1
            if k<0:
                return False
            k = max(k,nums[i])
        
        return True
                
            
        
        