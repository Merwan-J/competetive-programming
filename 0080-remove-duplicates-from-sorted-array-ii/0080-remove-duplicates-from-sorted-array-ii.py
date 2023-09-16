class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
         
        l = 1
        count = 1
        
        for r in range(1,len(nums)):
            if nums[r] != nums[l-1]:
                nums[l] = nums[r]
                count = 1 
                l+=1 
            
            elif nums[r] == nums[l-1] and count<2:
                nums[l] = nums[r]
                count+=1 
                l+=1 
        
        return l
                