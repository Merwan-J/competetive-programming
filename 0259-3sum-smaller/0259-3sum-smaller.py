class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        
        
        
        nums.sort()
        count = 0
        
        for i,num in enumerate(nums):
            for j in range(i+1,len(nums)):
                num2 = nums[j]
                compliment = target - 1 - (num+num2)
                pos = bisect_right(nums,compliment,j+1)
                count+= pos- (j + 1) 
                
        
        return count
        
        