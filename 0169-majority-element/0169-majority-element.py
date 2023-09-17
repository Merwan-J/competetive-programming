class Solution:
    def majorityElement(self, nums: List[int]) -> int:
    
        count = 0
        candidate = nums[0]
        
        for num in nums:
            
            if count == 0:
                candidate = num
            
            if candidate == num:
                count+=1
            else:
                count-=1
                
        return candidate
                
                