class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        
        
        count = 0
        l = 0
        
        for r in range(len(nums)):
            if nums[r]:
                l = r + 1 
            count += r - l + 1
        
        return count 
        
        
        