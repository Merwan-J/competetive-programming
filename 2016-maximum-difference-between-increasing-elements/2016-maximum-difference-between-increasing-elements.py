class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        maxDiff = nums[1] - nums[0]
        curMin = nums[0]
        
        for i in range(1,len(nums)):
            maxDiff = max(maxDiff, nums[i] - curMin)
            curMin = min(curMin,nums[i])
        
        return maxDiff if maxDiff>0 else -1