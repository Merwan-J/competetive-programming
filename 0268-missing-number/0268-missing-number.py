class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        all_nums = len(nums)
        nums_given = 0
        
        for i,num in enumerate(nums):
            all_nums^=i
            nums_given^=num
        
        return all_nums^nums_given
    