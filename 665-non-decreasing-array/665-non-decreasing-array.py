class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        count = 0
        
        for i in range(n-1):
            if nums[i]<=nums[i+1]:
                continue
            
            if count:
                return False
            
            if i==0 or nums[i+1]>=nums[i-1]:
                nums[i] = nums[i+1]
            else:
                nums[i+1] = nums[i]
                
            count = 1
        
        return True
        