class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
#         nums = sorted(nums)
#         count = 0
#         for i in range(len(nums)-1):
#             if nums[i]>=nums[i+1]:
#                 count+= abs(nums[i]-nums[i+1])+1
#                 nums[i+1] += abs(nums[i]-nums[i+1])+1
        
#         return count
        
        nums.sort()
        count = 0
        
        print(nums)
        for i in range(1,len(nums)):
            if nums[i]<=nums[i-1]:
                v = abs(nums[i]-nums[i-1])+1
                count+=v
                nums[i]+=v
        return count