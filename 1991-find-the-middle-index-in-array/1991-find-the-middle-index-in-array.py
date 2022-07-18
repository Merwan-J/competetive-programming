class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        prefix = 0

        for i in range(len(nums)):
            suffix = total - prefix - nums[i]
            if prefix == suffix:
                return i
            prefix += nums[i]
    
        return -1