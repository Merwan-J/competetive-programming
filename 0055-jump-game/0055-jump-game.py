class Solution:
    def canJump(self, nums: List[int]) -> bool:     
        curJump = 0

        for i,jump in enumerate(nums):
            curJump-=1 
            curJump = max(curJump,jump)
            
            if curJump == 0: break
        
        
        return i == len(nums)-1
            